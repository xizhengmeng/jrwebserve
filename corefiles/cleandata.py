#!/usr/bin/env python
# coding:utf-8

import os,sys
import pymongo
import re

reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = pymongo.MongoClient("localhost",27017)
mydb = connection.Spider # new a database
comment = mydb.Comment # new a table
clencomment = mydb.CleanComment

cdbs = clencomment.find({})

idList = []

for item in cdbs:
    userReviewId = item['userReviewId']
    idList.append(userReviewId)

dbs = comment.find({})

for item in dbs:
    userReviewId = item['userReviewId']
    if userReviewId in idList:
        continue
    body = item.get('body')
    if len(body) > 10 and len(body) < 150 and 1.0*body.count('好')/len(body)*3 < 0.4:
        print 'clencomment insert new'
        print body
        print item['date']
    	clencomment.insert(item)


