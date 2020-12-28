# File Transfer Server

Simple file transfer server in Python.

## Install
```bash
pip3 install .
```

## Usage
```
Usage: filetransfer [OPTIONS] COMMAND [ARGS]...

  Simple file transfer server.

Options:
  --help  Show this message and exit.

Commands:
  recv    Receive files from server.
  send    Send a file to the server.
  server  Launch server.
```

### Server
```
Usage: filetransfer server [OPTIONS]

  Launch server.

Options:
  -h, --host TEXT       Server name or IP address  [default: localhost]
  -p, --port INTEGER    Server port  [default: 1234]
  -d, --directory PATH  Directory  [default: .]
  --help                Show this message and exit.
```

### Clients

#### Send
```
Usage: filetransfer send [OPTIONS] FILENAME

  Send a file to the server.

Options:
  -h, --host TEXT     Server name or IP address  [default: localhost]
  -p, --port INTEGER  Server port  [default: 1234]
  --help              Show this message and exit.
```

#### Recv
```
Usage: filetransfer recv [OPTIONS]

  Receive files from server.

Options:
  -h, --host TEXT       Server name or IP address  [default: localhost]
  -p, --port INTEGER    Server port  [default: 1234]
  -d, --directory PATH  Directory  [default: .]
  --help                Show this message and exit.
```

## Author
[Quentin Deschamps](quentindeschamps18@gmail.com)

## License
[MIT](https://choosealicense.com/licenses/mit/)
