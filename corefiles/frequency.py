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

cleanall = clencomment.find({})

jieba.load_userdict('../coredata/customdict.txt')

keyword = {}

for item in cleanall:	
    body = item['body']
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
    print item[0],item[1]     




