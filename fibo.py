# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:47:49 2016

@author: Claire
"""
# Here is a simple while loop that recreates the Fibonacci suite.
# It is just a script example we can use and modify in order to learn GitHub!

parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)