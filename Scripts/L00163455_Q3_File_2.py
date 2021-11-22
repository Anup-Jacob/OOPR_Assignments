# ---------------------------------

# File          : L00163455_Q4_File_2
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 22/11/2021
# Modified Date : 22/11/2021
# Description   : Python script to check the connection to SSH
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

import paramiko
import time
import re


# Open SSH connection to the device
def ssh_connection(ip):
    try:
        username = "L00163455"  # In an automation script read data from file
        password = "V@@va123"  # never hard code
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt\n")  # unix command to list directory contents and save to file
        time.sleep(1)
        vm_output = connection.recv(65535)

        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))

        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


if __name__ == '__main__':
    ssh_connection("192.168.182.128")  # ip address of my VM, adjust to suit


