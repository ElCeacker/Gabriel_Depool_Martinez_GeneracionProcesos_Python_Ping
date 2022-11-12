import platform
import subprocess

def myPing(host):
    parameter = '-n' if platform.system().lower()=='debian' else '-c'

    command = ['ping', parameter, '5', host]
    response = subprocess.call(command)

    return response


print(myPing("8.8.4.4"))