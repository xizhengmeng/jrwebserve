# -*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba

connection = MongoClient("localhost", 27017)
mydb = connection.Spider  # new a database
basedata = mydb.analysebasedata  # new a table
clencomment = mydb.CleanComment

basedata = mydb.analysebasedata  # new a table

basedbs = basedata.find({})

neglist = []
poslist = []
neulist = []

for item in basedbs:
    poslist = item['pos']
    neglist = item['neg']

dbs = clencomment.find({})
analyseList = []

for item in dbs:
    nominal = 0
    if len(item['forsearch']) > 30 or int(item['rating']) > 3:
        continue
    seg_list = jieba.cut(item['forsearch'])
    print '**************' + '%d' % item['rating']
    # print item['forsearch']
    for word in seg_list:
        if word in poslist:
           nominal = nominal - 1
        elif word in neglist:
           nominal = nominal + 1
    print item['forsearch'],nominal

#clencomment.remove({})

#for item in analyseList:
#    clencomment.save(item)