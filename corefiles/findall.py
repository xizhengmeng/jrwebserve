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

command = sys.argv[1]

dbs = clencomment.find({})

#dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(10).skip(20)
#dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(20)
#dbs = comment.find({'body':re.compile('不好')})

idList = []

count = 0
for item in dbs:
    if item['userReviewId'] in idList:
        print 'repeat' + item['body'] + item['date'] + item['userReviewId']
    else:
        print item['body'] + item['date'] + item['userReviewId']
        count = count + 1

print count
