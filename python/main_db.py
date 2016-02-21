#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None
id = sys.argv[1]
try:

    con = psycopg2.connect(database='vagrant', user='vagrant')
    cur = con.cursor()
    cur.execute('SELECT * from users where user_id = %s', (id,))
    ver = cur.fetchone()
    print ver


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:

    if con:
        con.close()
print "زيد"
