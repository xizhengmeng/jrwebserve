# -*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba

connection = MongoClient("localhost", 27017)
mydb = connection.Spider  # new a database
basedata = mydb.analysebasedata  # new a table
clencomment = mydb.CleanComment

dbs = clencomment.find({})
analyseList = []

for item in dbs:
    nominal = 0
    if len(item['body']) > 30 or int(item['rating']) > 3:
        continue
    seg_list = jieba.cut(item['forsearch'])
    print '**************' + item['rating']
    print item['forsearch']
    for word in seg_list:
        print word
    baseitems = basedata.find({'title': word})
    if baseitems.count() > 0:
        baseitem = baseitems[0]
        itemnominal = baseitem.get('nominal')
        nominal = nominal + itemnominal
        print itemnominal, word
    print item['body'],nominal

#clencomment.remove({})

#for item in analyseList:
#    clencomment.save(item)