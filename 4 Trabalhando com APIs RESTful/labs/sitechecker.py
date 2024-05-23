import json
import os
import socket
import sys


exit_code = 0
if len(sys.argv) not in [2, 3]:
    print('Improper number of arguments: at least one is required and not more than are allowed:'
          '\n- http serve\'s address (required)'
          '\n- port number (defaults to 80 if not specified)')
    exit_code = 1
elif len(sys.argv) > 2 and (not sys.argv[2].isdigit() or not 1 <= int(sys.argv[2]) <= 65535):
    print(f'Port number is invalid {sys.argv[2]}')
    exit_code = 2
else:
    try:
        address = sys.argv[1]
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 80
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address, port))
        sock.send(b"GET / HTTP/1.1\r\nHost: " + bytes(address, 'utf-8') + b"\r\nConnection: close\r\n\r\n")
        answer = sock.recv(1024).decode('utf-8').split('\n')[0]
        print(answer)
        sock.close()
    except socket.timeout:
        print("Time out")
        exit_code = 3
    except socket.error:
        print("Other Error")
        exit_code = 4

exit(exit_code)
