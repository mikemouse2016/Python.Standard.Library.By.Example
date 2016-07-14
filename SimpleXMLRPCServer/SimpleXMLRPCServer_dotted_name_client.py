#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9000')
print 'BEFORE       :', 'EXAMPLE' in proxy.dir.list('/tmp')
print 'CREATE       :', proxy.dir.create('/tmp/EXAMPLE')
print 'SHOULD EXIST :', 'EXAMPLE' in proxy.dir.list('/tmp')
print 'REMOVE       :', proxy.dir.remove('/tmp/EXAMPLE')
print 'AFTER        :', 'EXAMPLE' in proxy.dir.list('/tmp')
