#!/usr/bin/env python
from yaml import load
import pprint
import json

print "Hello World"

f = open('data.yaml')
data = f.read()

data2 = load(data)
#pprint.pprint(data2)

print data2['items'][0]['price']
print json.dumps(data2)
