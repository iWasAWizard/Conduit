import pexpect
import paramiko
from classes.actions import Action, Verify
import regex as re

@staticmethod
def remove_ansi_escape_sequences(text):
    ansi_escape_pattern = re.compile(r'''
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
        ''', re.VERBOSE)

class ConduitSSH:
    def __init__(self, hostname, port=22, username=None, password=None, key_filename=None, logfile='ssh_log.txt'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.logfile = logfile

    def __enter__(self):
        self.log = open(self.logfile, 'a')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.hostname, port=self.port, username=self.username, password=self.password, key_filename=self.key_filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
        self.log.close()

    @staticmethod
    def remove_ansi_escape_sequences(text):
        ansi_escape_pattern = re.compile(r'''
            \x1B  # ESC
            (?:   # 7-bit C1 Fe (except CSI)
                [@-Z\\-_]
            |     # or [ for CSI, followed by a control sequence
                \[
                [0-?]*  # Parameter bytes
                [ -/]*  # Intermediate bytes
                [@-~]   # Final byte
            )
        ''', re.VERBOSE)
        return ansi_escape_pattern.sub('', text)

class SSHAction(Action):
    
    def execute_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        stdout_data = stdout.read().decode()
        stderr_data = stderr.read().decode()
        self.log.write(f"COMMAND: {command}\nOUTPUT: {stdout_data}\nERROR: {stderr_data}\n")
        return stdout_data, stderr_data

    def interactive_session(self, command, timeout=30):
        child = pexpect.spawn(f'ssh {self.username}@{self.hostname} -p {self.port}', encoding='utf-8')
        child.logfile = self.log

        if self.password:
            child.expect('password:')
            child.sendline(self.password)
        
        child.expect('$')
        child.sendline(command)

        try:
            child.expect(pexpect.EOF, timeout=timeout)
            output = child.before
        except pexpect.TIMEOUT:
            child.terminate()
            output = child.before
            error = 'Command timed out'
        
# Example usage:
# with ConduitSSHModule(hostname='example.com', username='user', password='password') as ssh:
#     output, error = ssh.execute_command('ls -l')
#     print('Output:', output)
#     print('Error:', error)
#     interactive_output, interactive_error = ssh.interactive_session('ls -l')
#     print('Interactive Output:', interactive_output)
#     print('Interactive Error:', interactive_error)

