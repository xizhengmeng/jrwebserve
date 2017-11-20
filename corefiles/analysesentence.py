# -*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba,time

reload(sys)
sys.setdefaultencoding( "utf-8" )

time1 = time.time()

connection = MongoClient("localhost", 27017)
mydbs = connection.Spider  # new a database
clencomment = mydbs.CleanComment

neglist = open('../coredata/neg.txt').read().split('\n')
poslist = open('../coredata/pos.txt').read().split('\r')
neulist = []

abpost = ['非常满意','强烈好评','值得信赖的京东','京东支持','感谢','谢谢','支持京东','强哥','给你好评','放心的京东','会一直支持的','会支持的','信赖京东','京东越来越好']
jieba.load_userdict('../coredata/customdict.txt')

count = 0

for i in range(20):
    dbs = clencomment.find({}).limit(1000).skip(i*1000)
    analyseList = []
    if dbs.count(True) == 0:
       time2 = time.time()
       print '退出'
       print count
       print 'usetime',time2 - time1
       sys.exit(1)
    for item in dbs:
        if item.get('hasanalyse') == True:
           continue
        nominal = 0
        #if len(item['forsearch']) > 100 or int(item['rating']) > 3:
        #   continue
        forsearch = item['forsearch']
        count = count + 1
        isAbsuPos = False
        for setence in abpost:
            if setence in forsearch:
               print 'abpos'+forsearch
               isAbsuPos = True

        if isAbsuPos:
           item['hasanalyse'] = True
           item['isneg'] = False
           clencomment.remove({'userReviewId':item['userReviewId']})
           clencomment.insert(item)
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
                   if lastitem == '无' or lastitem == '不' or lastitem == '没有' or lastitem == '非' or lastitem == '不是':
                       print 'fei' + lastitem + word
                   else:
                       print '2'+word
                       nominal = nominal - 1
               else:
                   nominal = nominal - 1
            else:
               #print '3'+word
               pass
        item['hasanalyse'] = True
        item['nominal'] = '%d' % nominal
        if nominal < 0:
           item['isneg'] = True
        else:
           item['isneg'] = False
        clencomment.remove({'userReviewId':item['userReviewId']})
        clencomment.insert(item)
        if nominal != 0:
           print 'neg',item['isneg'],item['forsearch']



