#!/usr/bin/env python
# coding:utf-8

import os,sys
import pymongo
import re
from bayes.bayes import *

reload(sys)
sys.setdefaultencoding( "utf-8" )

def checkIfisuseful(string,date):
    if len(string) > 10 and len(string) < 150:
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
                print '-------------------'
                print date,key,percent
                print string
                print '*******************'
                return False

        return isUseful(unitext)
    else:
        return False

connection = pymongo.MongoClient("localhost",27017)
mydb = connection.Spider # new a database
comment = mydb.Comment # new a table
clencomment = mydb.CleanComment

#clencomment.remove({})
#sys.exit(1)

cdbs = clencomment.find({}).sort([('date', -1)])

idList = []

for item in cdbs:
    userReviewId = item['userReviewId']
    idList.append(userReviewId)

dbs = comment.find({})

for item in dbs:
    userReviewId = item['userReviewId']
    if userReviewId not in idList:
       body = item.get('body')
       date = item.get('date')
       if checkIfisuseful(body,date) == True:
          print 'clencomment insert new ' + item['date'] + body
          forsearch = body + item['title']
          forsearch = forsearch.lower()
          forsearch = forsearch.replace(' ','')
          item['forsearch'] = forsearch

          if type(forsearch) == type(None):
              continue

          mode = testModel(forsearch)

          item['hasanalyse'] = True
          if mode == 1:
              item['isneg'] = True
          else:
              item['isneg'] = False

          clencomment.save(item)
          idList.append(item['userReviewId'])


