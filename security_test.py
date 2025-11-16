# SECURITY_TEST: contains insecure patterns
import subprocess

PASSWORD = "P@ssw0rd123"  # hardcoded secret
def run_user_code(code_str):
    # insecure
    return eval(code_str)

def call_shell(cmd):
    subprocess.Popen(cmd, shell=True)  # shell=True is dangerous
