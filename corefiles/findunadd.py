#!/usr/bin/env python
# coding:utf-8
import os,sys
import pymongo
import re
import jieba

reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = pymongo.MongoClient("localhost",27017)
mydb = connection.Spider # new a database
clencomment = mydb.CleanComment
basedata = mydb.analysebasedata  # new a table

dbs = basedata.find({})

neglist = []
poslist = []
neulist = []


for item in dbs:
    neulist = item['neu']
    poslist = item['pos']
    neglist = item['neg']

cleanall = clencomment.find({})

keyword = {}

for item in cleanall:
    body = item['forsearch']
    seg_list = seg_list = jieba.cut(body)
    for word in seg_list:
    	count = keyword.get(word)
        if type(count) == type(None):
            count = 1
            keyword[word] = count
        else:
            count = count + 1
            keyword[word] = count

resultDict = sorted(keyword.items(), key=lambda d:d[1], reverse = True)

for item in resultDict:
    word = item[0]
    if word not in neulist and word not in poslist and word not in neglist:
       print word,item[1]

    # print item[0],item[1]




