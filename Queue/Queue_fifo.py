#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""FIFO Queue
"""

import Queue

q = Queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get(),
print

