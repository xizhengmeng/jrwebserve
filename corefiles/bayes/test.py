#!/usr/bin/env python
# coding:utf-8
import os,sys

from bayes import *
testingNB()

# abpath = sys.path[0] + '/'
# if 'bayes/' not in abpath:
# 	abpath = abpath+'bayes/'
#
# # flist = open(abpath+'negtest.txt','r').read().split('\n')
#
# flist = open(abpath + 'postest.txt','r').read().split('\n')
#
# count = 0
#
# for line in flist:
# 	newlinw = translate(line)
# 	mode = testModel(newlinw)
# 	if mode == 1:
# 		count = count + 1
# 		print newlinw
#
#
# print '\n'
# print '\n'
# print '正确率 %f' % ((1.0 * (len(flist) - count)) / len(flist) * 100)
