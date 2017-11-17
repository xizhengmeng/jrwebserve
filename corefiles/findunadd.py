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
#clencomment = mydb.Comment
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

for item in cleanall:
    body = item['body']
    seg_list = jieba.cut(body)
    for word in seg_list:
        if word not in neulist and word not in poslist and word not in neglist:
            print word





