#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple example using doctest
"""

def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
