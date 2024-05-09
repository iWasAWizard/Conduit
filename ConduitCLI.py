import subprocess
import re

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

class ConduitCLI:
    def __init__(self, logfile='cli_log.txt'):
        self.logfile = logfile

    def __enter__(self):
        self.log = open(self.logfile, 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log.close()

    def execute_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8')
        stdout, stderr = process.communicate()
        stdout = remove_ansi_escape_sequences(stdout)
        stderr = remove_ansi_escape_sequences(stderr)
        return stdout, stderr
