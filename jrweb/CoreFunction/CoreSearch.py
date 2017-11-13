# -*- coding: utf-8 -*-

import os, time, json ,sys
from pymongo import MongoClient
import re

reload(sys)
sys.setdefaultencoding("utf-8")

connection = MongoClient("localhost", 27017)
mydb = connection.Spider  # new a database
comment = mydb.Comment  # new a table


def searchComment(searchkey, sorekey, pageindex, pagesize):
    if type(searchkey) == type(None):
        searchkey = ''

    if type(sorekey) == type(None):
        sorekey = 'date'

    if type(pagesize) == type(None):
        pagesize = 10
    else:
        pagesize = int(pagesize, 10)

    if type(pageindex) != type(0):
       pageindex = int(pageindex,10)

    skipnumber = pagesize * pageindex

    dbs = comment.find({'body': re.compile(searchkey)}).sort([('date',1)]).limit(pagesize).skip(skipnumber)
    # dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(20).skip(10)

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

