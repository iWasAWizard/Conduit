with ConduitCLI(logfile='cli_operations.log') as cli:
    try:
        output = cli.execute_command("ls -l")
        print("CLI Output:", output)
    except RuntimeError as e:
        print("An error occurred:", e)

#######################################################################

with ConduitSSHModule(hostname="192.168.1.100",
                      username="user",
                      password="password",
                      logfile='ssh_operations.log') as ssh:
    try:
        output, error = ssh.execute_command("ls -l")
        print("SSH Output:", output)
        if error:
            print("SSH Error:", error)
    except RuntimeError as e:
        print("An error occurred:", e)
