#!/usr/bin/env python
# coding:utf-8
import os,sys
import pymongo
import re
import time
import datetime

reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = pymongo.MongoClient("localhost",27017)
mydb = connection.Spider # new a database
comment = mydb.Comment # new a table
clencomment = mydb.CleanComment

dbs = clencomment.find({'userReviewId':'1878815456'})

for item in dbs:
    print item
    clencomment.remove({'userReviewId':item['userReviewId']})
    item['isneg'] = True
    print item
    clencomment.insert(item)