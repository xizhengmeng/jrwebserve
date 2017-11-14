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

keyword = {}

for item in cleanall:
	body = item['body']
    seg_list = seg_list = jieba.cut(body)  # 搜索引擎模式
    for word in seg_list:
    	count = keyword.get(word)
        if type(count) == type(None):
            count = 1
            keyword[word] = count
        else:
            count = count + 1
            keyword[word] = count

resultDict = sorted(keyword.items(), key=lambda d:d[1], reverse = True)

for item in resultDict.keys():
    print item,resultDict.get(item)     




