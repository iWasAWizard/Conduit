from modules.ssh import ssh
from modules.cli import cli

from classes.actions import Action
from classes.verifiers import Verify

action = Action()
verify = Verify()

def main():
    with cli.ConduitCLI() as cli1:
        cli1.act.execute_command("echo hello world local!")

    with ssh.ConduitSSH(hostname="10.0.0.6", username="joey", password="1qaz2wsx") as ssh1:
        ssh1.act.execute_command("echo hello world remote!")

if __name__== "__main__":
    main()
