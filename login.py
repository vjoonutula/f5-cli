#!/usr/bin/env python
'''
'''
import bigsuds
import getpass
import sys
import base64
import pprint

host = 'f5-1b.dev.b.chicken.net'
print "\nUsername: " 
user = 'john6150'
print "\nHey %s, please enter your password below.\n" % user
upass = getpass.getpass()

try:   
    b = bigsuds.BIGIP(
        hostname = host, 
        username = user, 
        password = upass,
        )
    bclient = b.with_session_id()
    bclient.System.Session.set_transaction_timeout(60)
    bclient.System.Session.set_active_folder('/CI_Engineers')
except Exception, e:
    print e


