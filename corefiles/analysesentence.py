# -*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba


reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = MongoClient("localhost", 27017)
mydb = connection.database  # new a database
basedata = mydb.analysebasedata  # new a table

mydbs = connection.Spider  # new a database
clencomment = mydbs.CleanComment

basedata = mydb.analysebasedata  # new a table

basedbs = basedata.find({})

neglist = []
poslist = []
neulist = []

for item in basedbs:
    poslist = item['pos']
    neglist = item['neg']

for i in range(15):
    dbs = clencomment.find({}).limit(1000).skip(1)
    analyseList = []

    for item in dbs:
        nominal = 0
        #if len(item['forsearch']) > 100 or int(item['rating']) > 3:
        #   continue
        seg_list = jieba.cut(item['forsearch'])
        print '**************' + '%d' % item['rating']
        # print item['forsearch']
        for word in seg_list:
            if word in poslist:
               #print word,'1'
               pass
            elif word in neglist:
               print word, '-1'
               nominal = nominal - 1
        if nominal != 0 and item['rating'] == 5:
           print item['forsearch'],nominal

#clencomment.remove({})

#for item in analyseList:
#    clencomment.save(item)