# -*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba


reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = MongoClient("localhost", 27017)
mydbs = connection.Spider  # new a database
clencomment = mydbs.CleanComment

neglist = open('../coredata/neg.txt').read().split('\n')
poslist = open('../coredata/pos.txt').read().split('\r')
neulist = []

abpost = ['感谢','谢谢','支持京东','强哥','给你好评','放心的京东','会一直支持的','会支持的','信赖京东','京东越来越好']
jieba.load_userdict('../coredata/customdict.txt')

for i in range(2):
    dbs = clencomment.find({}).limit(1000).skip(i*1000)
    analyseList = []

    for item in dbs:
        nominal = 0
        #if len(item['forsearch']) > 100 or int(item['rating']) > 3:
        #   continue
        forsearch = item['forsearch']

        isAbsuPos = False
        for setence in abpost:
            if setence in forsearch:
               print 'abpos'+forsearch
               isAbsuPos = True

        if isAbsuPos:
           continue

        seg_list = jieba.cut(forsearch)

        seg_listnew = []

        for seg in seg_list:
            seg_listnew.append(seg)

        for word in seg_listnew:
            if word in poslist:
               #print '1'+word
               pass
            elif word in neglist:
               lastindex = seg_listnew.index(word) - 1
               if lastindex >= 0:
                   lastitem = seg_listnew[lastindex]
                   print 'last'+lastitem
                   if lastitem == '不' or lastitem == '没有' or lastitem == '非' or lastitem == '不是':
                       print 'fei' + lastitem + word
                   else:
                       print '2'+word
                       nominal = nominal - 1
               else:
                   nominal = nominal - 1
            else:
               #print '3'+word
               pass
        if nominal != 0 and item['rating'] == 5:
           print 'neg'+item['forsearch']

#clencomment.remove({})

#for item in analyseList:
#    clencomment.save(item)