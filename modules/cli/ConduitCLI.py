import re
import pexpect

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

    def execute_command(self, command, timeout=30):
        child = pexpect.spawn(command, encoding='utf-8')
        child.logfile = self.log

        try:
            child.expect(pexpect.EOF, timeout=timeout)
            stdout = child.before
        except pexpect.TIMEOUT:
            child.terminate()
            stdout = child.before
            stderr = 'Command timed out'
        
        stdout = remove_ansi_escape_sequences(stdout)
        return stdout, stderr if 'stderr' in locals() else ''

    def sendline(self, command, expected_output=None, timeout=30):
        child = pexpect.spawn(command, encoding='utf-8')
        child.logfile = self.log
        
        if expected_output:
            child.expect(expected_output, timeout=timeout)
        child.sendline(command)
        
        try:
            child.expect(pexpect.EOF, timeout=timeout)
            stdout = child.before
        except pexpect.TIMEOUT:
            child.terminate()
            stdout = child.before
            stderr = 'Command timed out'
        
        stdout = remove_ansi_escape_sequences(stdout)
        return stdout, stderr if 'stderr' in locals() else ''

# Example usage:
# with ConduitCLI() as cli:
#     output, error = cli.execute_command('ls -l')
#     print('Output:', output)
#     print('Error:', error)
