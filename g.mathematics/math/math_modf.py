#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Split fractional from whole number part.
"""

import math

for i in range(6):
    print '{}/2 = {}'.format(i, math.modf(i/2.0))
