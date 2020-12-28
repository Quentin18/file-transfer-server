"""
CLI to transfer files.

Author: Quentin Deschamps
Date: 2020
"""
import click

from filetransfer.server import Server
from filetransfer.send import sendfile
from filetransfer.recv import recvfile


@click.group()
def cli():
    """Simple file transfer server."""
    pass


@cli.command()
@click.option('-h', '--host', type=click.STRING, default='localhost',
              show_default=True, help='Server name or IP address')
@click.option('-p', '--port', type=click.INT, default=1234,
              show_default=True, help='Server port')
@click.option('-d', '--directory', type=click.Path(), default='.',
              show_default=True, help='Directory')
def server(host, port, directory):
    """Launch server."""
    Server(port, directory, host)


@cli.command()
@click.option('-h', '--host', type=click.STRING, default='localhost',
              show_default=True, help='Server name or IP address')
@click.option('-p', '--port', type=click.INT, default=1234,
              show_default=True, help='Server port')
@click.argument('filename', type=click.Path(exists=True))
def send(host, port, filename):
    """Send a file to the server."""
    sendfile(host, port, filename)


@cli.command()
@click.option('-h', '--host', type=click.STRING, default='localhost',
              show_default=True, help='Server name or IP address')
@click.option('-p', '--port', type=click.INT, default=1234,
              show_default=True, help='Server port')
@click.option('-d', '--directory', type=click.Path(), default='.',
              show_default=True, help='Directory')
def recv(host, port, directory):
    """Receive files from server."""
    recvfile(host, port, directory)
