from conduit import cli, ssh
from program import my_custom_commands

##############################################################
#Snippet from program.my_custom_commands

def create_user(username, password):
    self.act.cli.send_keys("./my_tool")
    self.act.cli.send_keys("create user f'{username}'")
    self.verify.cli.response_contains(search_str="Created new user f'{username}'",
                                      silent=True)
    
def user_list_contains(search_str):
    self.act.cli.send_keys("list user")
    self.verify.cli.response_contains(search_str,
                                      silent=True)

##############################################################


# Refresh VM
for i in self.vmware.list_vms(host="my.esxi.local"):
    self.vmware.revert_to_snapshot(host=i)

@testcase
with self.ssh.connect(host="10.0.0.1",
                      user="user",
                      password="nicetry",
                      message="In a new terminal window, SSH into f'{host}' as f'{user}'") as ssh1:

    ssh1.act.cli.send(command="echo 'hello world'",
                      message="From the SSH prompt, execute the following command:\nf'{command}'",
                      silent=False)

    ssh1.verify.cli.find_match(search_str="hello world",
                               message="In the SSH prompt, confirm that the following string is present:\nf'{search_str}'",
                               silent=False)

    ssh1.act.my_custom_commands.create_user(username="user",
                                            password="nicetry",
                                            message="In the SSH prompt, open my_tool, and create a new user named f'{username}'",
                                            silent=False)

    ssh1.verify.my_custom_commands.user_list_contains(search_str="user",
                                                      message="Confirm that the new user was created by executing the following command:\nlist users",
                                                      silent=False)
