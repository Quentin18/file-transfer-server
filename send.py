"""
Client to send a file to the server.

Author: Quentin Deschamps
Date: 2020
"""
import sys
import os
import socket

BUFFER_SIZE = 1024
SEPARATOR = '<SEPARATOR>'
SEND_CODE = 'SEND'


def sendfile(host, port, filename):
    """Sends a file to the server."""
    # check if the file exists
    if not os.path.exists(filename):
        raise FileExistsError(f'File {filename} not found.')

    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    print(f'Connecting to {host}:{port}...')
    s.connect((host, port))
    print('Connected.')

    # send the code and the filename
    s.send(SEPARATOR.join([SEND_CODE, filename]).encode())
    reply = s.recv(BUFFER_SIZE).decode()

    if reply != 'file-accepted':
        print('The server refused the file.')

    else:
        # start sending the file
        print(f'Sending the file {filename}...')
        with open(filename, 'rb') as f:
            data = f.read(BUFFER_SIZE)
            while data:
                s.send(data)
                data = f.read(BUFFER_SIZE)
        print(f'File sent!')

    # close the socket
    s.close()
    print('Connexion closed.')


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 4:
        host = args[1]
        port = int(args[2])
        filename = args[3]
        sendfile(host, port, filename)
    else:
        print('Usage: python3 send.py [HOST] [PORT] [FILENAME]')
