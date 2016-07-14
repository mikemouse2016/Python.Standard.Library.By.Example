#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Combining dates and times into a single object.
"""

import datetime

print 'Now    :', datetime.datetime.now()
print 'Today  :', datetime.datetime.today()
print 'UTC Now:', datetime.datetime.utcnow()
print

FIELDS = [ 'year', 'month', 'day',
           'hour', 'minute', 'second', 'microsecond',
           ]

d = datetime.datetime.now()
for attr in FIELDS:
    print '%15s: %s' % (attr, getattr(d, attr))
