# ---------------------------------

# File          : L00163455_Q5_File_2.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 05/12/2021
# Modified Date : 05/12/2021
# Description   : Python script to connect to an Linux server and create folders via Python
# Licensing     : Anup Jacob, LYIT

# ----------------------------------

import time
import re
import paramiko

IP = '192.168.182.128'


def ssh_connection(user, passwd):
    # Function to open SSH connection to the device

    try:
        print("\nEstablishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # print(username)
        # print(password)
        session.connect(IP, username=user, password=passwd)
        connection = session.invoke_shell()
        # unix command to Create Lab 1 sub folder. The command automatically creates the parent folder Labs if do not
        # exists
        connection.send('mkdir -p Labs/Lab1\n')
        print('Labs folder created Successfully')
        time.sleep(1)
        print('Lab1 sub-folder created Successfully')
        # unix command to Create Lab 2 sub folder
        connection.send('mkdir -p Labs/Lab2\n')
        print('Lab2 sub-folder created Successfully')
        time.sleep(1)
        vm_output = connection.recv(65535)
        print(vm_output)

        # Error handling if found any
        if re.search(b"% Invalid input", vm_output):
            print("Sorry, Error Connecting to {}".format(IP))
        else:
            print("Commands successfully executed on the IP {}".format(IP))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")
        ssh_connection(user, passwd)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    print("******** Remote Connection ********")
    # Input taken from the user for connecting remotely
    username = input("\nEnter your Username : ")
    password = input("Enter your password : ")
    ssh_connection(username, password)
print('\n----- Thank you for using my application -----')
