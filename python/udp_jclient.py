#!/usr/bin/python           # This is client.py file
import json
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

request = {'command': 'upper',
'args': ['line1', 'line2', 'line3']
}
server_address = ('localhost', 10000)
message = json.dumps(request)


try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    res = json.loads(data)
    print "Server send: %s" % res

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
