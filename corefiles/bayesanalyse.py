# -*- coding: utf-8 -*-

import os ,sys
from pymongo import MongoClient
import jieba,time
from bayes.bayes import *

connection = MongoClient("localhost", 27017)
mydbs = connection.Spider  # new a database
clencomment = mydbs.CleanComment

time1 = time.time()

countn = 0

for i in range(20):
    dbs = clencomment.find({}).limit(1000).skip(i*1000)
    analyseList = []
    if dbs.count(True) == 0:
       time2 = time.time()
       print '退出'
       print countn
       print 'usetime',time2 - time1
       sys.exit(1)
    for item in dbs:
        if item.get('hasanalyse') == True:
           continue

        forsearch = item.get('forsearch')

        if type(forsearch) == type(None):
            continue

        mode = testModel(forsearch)
        countn = countn + 1

        item['hasanalyse'] = True
        if mode == 1:
           item['isneg'] = True
        else:
           item['isneg'] = False
        clencomment.remove({'userReviewId':item['userReviewId']})
        clencomment.insert(item)



