"""
Server to stock and transfer files to clients.

Author: Quentin Deschamps
Date: 2020
"""
import socket
import threading
import sys
import os.path
import logging

BUFFER_SIZE = 1024
BACKLOG = 10


def logger_config(level, name):
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add to logger
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


# create logger
logger = logger_config(level=logging.DEBUG, name='FileTransferServer')


class FileList:
    """Manage the ".files" file to stock the list of files."""
    def __init__(self, directory, name='.files'):
        self.directory = directory
        self.filename = os.path.join(directory, name)
        self.create_filelist()

    def create_filelist(self):
        """Create the ".files" file."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w'):
                pass

    def add(self, filename):
        """Add a filename to the filelist."""
        with open(self.filename, 'a') as f:
            f.write(filename + '\n')


class Server:
    """Manages the file transfer server."""
    def __init__(self, port, directory, host='0.0.0.0'):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        if not os.path.exists(directory):
            os.mkdir(directory)
        self.directory = directory
        self.filelist = FileList(directory)
        self.accept_connections()

    def accept_connections(self):
        """Loop method to accept connections."""
        self.s.bind((self.host, self.port))
        self.s.listen(BACKLOG)

        logger.debug(f'Listening as {self.host}:{self.port}')

        while True:
            conn, addr = self.s.accept()
            logger.debug(f'Client {addr} connected')

            # start new thread to receive a new file
            threading.Thread(
                target=self.handle_client, args=(conn, addr,)).start()

    def handle_client(self, conn, addr):
        """
        Method to manage a client thread and to receive a new file.
        """
        # receive filename
        filename = conn.recv(BUFFER_SIZE).decode()
        # keep only the basename of the file
        filename = os.path.basename(filename)
        conn.send('file-accepted'.encode())

        # start receiving the content of the file from the connection
        logger.debug(f'Receiving the file {filename}')
        with open(os.path.join(self.directory, filename), 'wb') as f:
            data = conn.recv(BUFFER_SIZE)
            while data:
                f.write(data)
                data = conn.recv(BUFFER_SIZE)

        logger.debug(f'File {filename} received')

        # add filename to the list
        self.filelist.add(filename)

        # close connection
        conn.close()
        logger.debug(f'Client {addr} disconnected')


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 3:
        port = int(args[1])
        directory = args[2]
        server = Server(port, directory)
    else:
        print('Usage: python3 server.py [PORT] [DIRECTORY]')
