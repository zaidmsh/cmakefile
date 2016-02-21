#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "zaidmsh.github.io" # Get local machine name
port = 80                # Reserve a port for your service.

request = """GET /index.html HTTP/1.1
Host: %s

""" % host

s.connect((host, port))
s.send(request)
print s.recv(1024)
s.close                     # Close the socket when done
