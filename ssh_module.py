import paramiko

class ConduitSSHModule:
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
        self.client.connect(self.hostname, port=self.port, username=self.username, key_filename=self.key_filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
        self.log.close()

    def execute_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()
