#!/usr/bin/env python
# coding:utf-8

import os, sys
import pymongo
import re

reload(sys)
sys.setdefaultencoding("utf-8")

connection = pymongo.MongoClient("localhost", 27017)
mydb = connection.Spider  # new a database
comment = mydb.CleanComment  # new a table
statistics = mydb.Statistics  # new a table

statistics.remove({})

# dbs = statistics.find({})

# for db in dbs:
# 	print db['statistic']

# dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(10).skip(20)

service = [{u'白条': 0}, {u'理财': 0}, {u'金条': 0}, {u'小金库': 0}, {u'信用': 0}, {u'支付': 0}, {u'还款': 0}, {u'借款': 0}, {u'信用卡': 0},
           {u'利息': 0}, {u'赎回': 0}, {u'提现': 0}, {u'提额': 0}, {u'分期': 0}]
experience = [{u'闪退': 0}, {u'体验': 0}, {u'界面': 0}, {u'操作': 0}, {u'安全': 0}, {u'登录': 0}, {u'速度': 0}]
other = [{u'商城': 0}, {u'客服': 0}, {u'支付宝': 0}, {u'垃圾': 0}]

dic = {}
dic['service'] = service
dic['experience'] = experience
dic['other'] = other

keys = dic.keys()
resultData = []

for key in keys:
    cureentDic = {'title':key}
    speList = []
    dicSpe = dic.get(key)
    for item in dicSpe:
        keyword = item.keys()[0]
        dbs = comment.find({'body': re.compile(keyword)})
        del item[keyword]
        item['content'] = keyword
        item['num'] = dbs.count()
        speList.append(item)
    cureentDic['list'] = speList
    resultData.append(cureentDic)

statistics.insert({'statistic': resultData})
