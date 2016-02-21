#!/usr/bin/python           # This is client.py file

import socket
import json

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

if True:
    request = {'command': 'upper',
    'args': ['line1', 'line2', 'line3']
    }
    s.send(json.dumps(request))
    data = s.recv(1024)
    res = json.loads(data)
    print "Server send: %s" % res

s.close                     # Close the socket when done
