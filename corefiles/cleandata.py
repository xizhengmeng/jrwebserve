#!/usr/bin/env python
# coding:utf-8

import os,sys
import pymongo
import re

reload(sys)
sys.setdefaultencoding( "utf-8" )

def checkIfisuseful(string):
    if len(body) > 10 and len(body) < 150:
        unitext = string
        if type(string) == type(''):
            unitext = unicode(string, 'utf-8')

        stringlist = unitext
        dic = {}
        for item in stringlist:
            count = dic.get(item)
            if type(count) == type(None):
                count = 1
                dic[item] = count
            else:
                count = count + 1
                dic[item] = count
        keys = dic.keys()
        total = 0
        for key in keys:
            count = dic.get(key)
            total = count + total
        for key in keys:
            count = dic.get(key) * 1.0
            percent = count / total
            if percent > 0.3:
                print '------------smart'
                print key, percent
                print string
                print '------------smart'
                return False
        return True

    else:
        return False

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
    if checkIfisuseful(body) == True:
       print 'clencomment insert new'
       print body
       print item['date']
       clencomment.insert(item)


