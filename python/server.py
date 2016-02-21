#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

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
        lines = data.split("\n")
        print lines
        command = lines[0]
        args = lines[1:]
        if command == "upper":
            data = ""
            for arg in args:
                data += arg.upper() + "\n"
        else:
            data = ""
            for arg in args:
                data += arg.lower() + "\n"

        c.send(data)

    c.close()                # Close the connection
