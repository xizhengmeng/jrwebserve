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
        return 'input searchkey'

    if type(sorekey) == type(None):
        sorekey = 'date'

    if type(pagesize) == type(None):
        pagesize = 10

    if type(pageindex) != type(0):
       pageindex = int(pageindex,10)

    skipnumber = pagesize * pageindex

    dbs = comment.find({'body': re.compile(searchkey)}).sort([('date',1)]).limit(pagesize).skip(skipnumber)
    # dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(20).skip(10)

    list = []
    for item in dbs:
        dic = {}
        dic['userReviewId'] = item.get('userReviewId')
        dic['body'] = item.get('body')
        dic['date'] = item.get('date')
        dic['name'] = item.get('name')
        dic['rating'] = item.get('rating')
        dic['title'] = item.get('title')
        dic['time'] = item.get('time')

        list.append(dic)
    liststring = json.dumps(list)
    return liststring

