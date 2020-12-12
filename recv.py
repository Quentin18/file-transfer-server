"""
Client to receive files not recovered from the server.

Author: Quentin Deschamps
Date: 2020
"""
import sys
import os
import socket
import zipfile

BUFFER_SIZE = 1024
RECV_CODE = 'RECV'
ZIP_NAME = 'data.zip'


def recvfile(host, port, directory):
    """Receives files not recovered from the server."""
    # create directory if it does not exists
    if not os.path.exists(directory):
        os.mkdir(directory)

    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    print(f'[+] Connecting to {host}:{port}...')
    s.connect((host, port))
    print('[+] Connected.')

    # send action code to the server
    s.send(RECV_CODE.encode())
    reply = s.recv(BUFFER_SIZE).decode()

    if reply != 'recovering':
        print('[+] Exit.')

    else:
        # create zip file with revovered files
        zip_name = os.path.join(directory, ZIP_NAME)
        print('[+] Receiving the files...')
        with open(zip_name, 'wb') as f:
            data = s.recv(BUFFER_SIZE)
            while data:
                f.write(data)
                data = s.recv(BUFFER_SIZE)

        # extract files
        print('[+] Extracting the files...')
        with zipfile.ZipFile(zip_name, 'r') as f:
            f.extractall(directory)

        print('[+] Done')

        # remove zip file
        os.remove(zip_name)

    # close the socket
    s.close()
    print('[+] Connexion closed.')


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 4:
        host = args[1]
        port = int(args[2])
        directory = args[3]
        recvfile(host, port, directory)
    else:
        print('Usage: python3 recv.py [HOST] [PORT] [DIRECTORY]')
