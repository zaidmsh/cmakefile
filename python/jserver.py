#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import json

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    c.send('Thank you for connecting\n')
    while True:
        data = c.recv(1024)
        if not data:
            break
        if data.strip() == "quit":
            break
        req = json.loads(data)
        print "req: %s" % req

        if req['command'] == "upper":
            data = [ x.upper() for x in req['args'] ]
        else:
            data = [ x.lower() for x in req['args'] ]
        c.send(json.dumps(data))

    c.close()                # Close the connection
