#!/usr/bin/env python
# coding:utf-8
import os,sys

from bayes import *
import numpy

abpath = sys.path[0] + '/'
if 'bayes/' not in abpath:
	abpath = abpath+'bayes/'
# testingNB()

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

myVocabList = numpy.load(abpath + "t.npy").tolist()
p0V = numpy.load(abpath + "a.npy")
p1V = numpy.load(abpath + "b.npy")
pAb = numpy.load(abpath + "c.npy")

P = p1V

for i in range(1000):
	print numpy.amax(P),numpy.argmax(P),myVocabList[numpy.argmax(P)]
	P[numpy.argmax(P)] = -20.0

# print numpy.argmax(p0V)
# print numpy.max(p0V)
# print p0V[numpy.argmax(p0V)]
# print myVocabList[numpy.argmax(p0V)]
# print numpy.where(numpy.max(p0V))[0][0]





