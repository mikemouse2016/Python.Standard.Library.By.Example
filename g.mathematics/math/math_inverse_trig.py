#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Inverse trigonometric functions
"""

import math

for r in [ 0, 0.5, 1 ]:
    print 'arcsine(%.1f)    = %5.2f' % (r, math.asin(r))
    print 'arccosine(%.1f)  = %5.2f' % (r, math.acos(r))
    print 'arctangent(%.1f) = %5.2f' % (r, math.atan(r))
    print
