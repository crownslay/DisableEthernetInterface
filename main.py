import os
import subprocess

def check_interface():
    output = subprocess.check_output('netsh interface show interface Ethernet | findstr Administrative', shell=True)
    status=output.decode("UTF-8")

    if "Enabled" in status:
        return True
    else:
        return False

def disable_interface(admin_status):
    if admin_status == True:
        os.system('cmd /c "netsh interface set interface Ethernet Disable')
    else:
        os.system('cmd /c "netsh interface set interface Ethernet Enable"')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    status = check_interface()
    disable_interface(status)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
