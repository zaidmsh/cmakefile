#!/usr/bin/python           # This is server.py file
import socket               # Import socket module
import json
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)

    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    req = json.loads(data)
    print "req: %s" % req

    if req['command'] == "upper":
        data = [ x.upper() for x in req['args'] ]
    else:
        data = [ x.lower() for x in req['args'] ]

    if data:
        sent = sock.sendto(json.dumps(data), address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
