# -*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba


reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = MongoClient("localhost", 27017)
mydbs = connection.Spider  # new a database
clencomment = mydbs.CleanComment

neglist = open('../coredata/neg.txt').read().split('\r')
poslist = open('../coredata/pos.txt').read().split('\r')
neulist = []

abpost = ['感谢','谢谢','好评','强哥','给你好评']
jieba.load_userdict('../coredata/customdict.txt')

for i in range(15):
    dbs = clencomment.find({}).limit(1000).skip(1)
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

        for word in seg_list:
            if word in poslist:
               print '1'+word
            elif word in neglist:
               print '2'+word
               nominal = nominal - 1
        # if nominal != 0 and item['rating'] == 5:
        #    print item['forsearch'],nominal

#clencomment.remove({})

#for item in analyseList:
#    clencomment.save(item)