#!/usr/bin/env python
# coding:utf-8
import os,sys

from bayes import *
# testingNB()

flist = open('negtest.txt','r').read().split('\n')
# flist = open('postest.txt','r').read().split('\n')

count = 0

for line in flist:
	mode = testModel(line)
	if mode == 0:
		count = count + 1

print '\n'
print '\n'
print '正确率 %f' % ((1.0 * (len(flist) - count)) / len(flist) * 100)
