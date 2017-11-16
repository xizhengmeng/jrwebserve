# -*- coding: utf-8 -*-

import os, time, json ,sys
from pymongo import MongoClient
import re
import logging
#
logger = logging.getLogger('sourceDns.webdns.views')

reload(sys)
sys.setdefaultencoding("utf-8")

connection = MongoClient("localhost", 27017)
mydb = connection.Spider  # new a database
#comment = mydb.Comment  # new a table
clencomment = mydb.CleanComment
statistics = mydb.Statistics  # new a table

def searchComment(searchkey, sorekey, pageindex, pagesize):
    if type(searchkey) == type(None):
        searchkey = ''

    if type(sorekey) == type(None):
        sorekey = 'date'

    if type(pagesize) == type(None):
        pagesize = 10
    else:
        if type(pagesize) == type(u'0'):
           pagesize = int(pagesize, 10)

    if type(pageindex) == type(None):
        pageindex = 1
    else:
       if type(pageindex) == type(u'0'):
          pageindex = int(pageindex,10)

    if type(pageindex) != type(0):
        return 'pageindex type wrong'

    if type(pagesize) != type(0):
        return 'pagesize type wrong'

    skipnumber = pagesize * pageindex

    dbs = clencomment.find({'body': re.compile(searchkey)}).sort([('date',-1)]).limit(pagesize).skip(skipnumber)

    list = []
    for item in dbs:
        dic = {}
        dic['evaluateId'] = item.get('userReviewId')
        dic['content'] = item.get('body')
        dic['time'] = item.get('date')
        dic['userName'] = item.get('name')
        dic['score'] = item.get('rating')
        dic['title'] = item.get('title')
        dic['scondtime'] = item.get('time')

        list.append(dic)

    resultDic = {}
    resultDic['resultData'] = list
    resultDic['code'] = '0000'
    liststring = json.dumps(resultDic)

    return liststring

def createKeyWordList():
    dbs = statistics.find({})
    list = []
    for db in dbs:
        list = db['statistic']

    resultDic = {}
    resultDic['resultData'] = list
    resultDic['code'] = '0000'

    resultString = json.dumps(resultDic)

    return resultString
