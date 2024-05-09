# Example of using the Conduit framework to execute tests and post results to SquashTM

# Initialize the CLI and SSH modules
with ConduitCLI(logfile='cli_output.log') as cli, ConduitSSHModule(hostname="example.com", username="root", password="password", logfile='ssh_output.log') as ssh:
    # Execute a command locally and remotely
    local_output = cli.execute_command("echo 'Running local diagnostics'")
    ssh_output, ssh_error = ssh.execute_command("echo 'Running remote diagnostics'")

    # Check outputs and handle accordingly
    if "Error" in ssh_error:
        print("Error encountered in SSH command:", ssh_error)
    print("Local diagnostics output:", local_output)
    print("Remote diagnostics output:", ssh_output)

# Post results to SquashTM
squash = ConduitSquashTMIntegration(base_url="http://api.squashtm.example.com", auth_token="your_auth_token")
test_result = {
    "test_id": "001",
    "status": "passed",
    "details": local_output + " and " + ssh_output
}
status_code, response = squash.post_test_result(project_id="12345", test_result=test_result)
if status_code == 200:
    print("Successfully posted results to SquashTM:", response)
else:
    print("Failed to post results to SquashTM:", response)
