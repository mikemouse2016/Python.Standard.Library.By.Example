#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using ifilter()

"""

from itertools import *

def check_item(x):
    print 'Testing:', x
    return (x<1)

for i in ifilter(check_item, [ -1, 0, 1, 2, -2 ]):
    print 'Yielding:', i
