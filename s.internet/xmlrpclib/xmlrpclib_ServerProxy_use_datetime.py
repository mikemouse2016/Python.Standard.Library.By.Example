#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000', use_datetime=True)
now = server.now()
print 'With:', now, type(now), now.__class__.__name__

server = xmlrpclib.ServerProxy('http://localhost:9000', use_datetime=False)
now = server.now()
print 'Without:', now, type(now), now.__class__.__name__
