import os
import traceback
import subprocess
from datetime import datetime

# Execute cv.
# If the server is not running, expect a general exception.
def syscmd(cmdline):
    stderr = subprocess.STDOUT
    output = subprocess.check_output(cmdline, shell=True, timeout=100, stderr=stderr)
    return output.decode()


def cv(cmd):
    cmdline = 'cv ' + cmd
    #cmdline = 'cv /c 127.0.0.1 /t 5 /w 5 ' + cmd
    resp = syscmd(cmdline)
    # print(resp)
    hdr = 'Received: Success'
    if hdr not in resp:
        return -1
    else:
        return resp


# Function for CV commands
def servercommand(cmd):
    serverResp = cv(cmd)
    # print(serverResp)
    if serverResp == -1:
    #if cv(cmd) < 0:
        print('{} failed'.format(cmd))
    return serverResp

def work():
    serverReply = servercommand('getlibrary')
    currentLibrary = serverReply.splitlines()[3].split('= ')[1]
    print(currentLibrary)
    servercommand('videoinput Broadcast Single 0 0 SDI SDI SDI 0')
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    print(dt_string)
    print('record {} {} -1 1 0 1'.format(currentLibrary, dt_string))
    servercommand('record {} {} -1 1 0 1'.format(currentLibrary, dt_string))




def main():
    try:
        work()
        return 0
    except Exception:
        # Print a trackback of a coding error
        print(traceback.format_exc())
        return 1


if __name__ == "__main__":
    main()
