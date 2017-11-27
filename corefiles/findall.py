#!/usr/bin/env python
# coding:utf-8
import os,sys
import pymongo
import re
import time
import datetime

reload(sys)
sys.setdefaultencoding( "utf-8" )

time1 = time.time()

connection = pymongo.MongoClient("localhost",27017)
mydb = connection.Spider # new a database
comment = mydb.Comment # new a table
clencomment = mydb.CleanComment

idList = []
countn = 0
for i in range(30):
    dbs = clencomment.find({'isneg':True}).sort([('date', -1)]).limit(1000).skip(i*1000)
    
    now_time = datetime.datetime.now()
    now_time_string = now_time.strftime('%Y-%m-%d')
    yes_time = now_time + datetime.timedelta(days=-10)
    yes_time_nyr = yes_time.strftime('%Y-%m-%d')

    print now_time_string,yes_time_nyr

    #dbs = clencomment.find({"date": {"$gte": yes_time_nyr, "$lt": now_time_string}})

    print 'count',dbs.count,i*1000
    if dbs.count(True) == 0:
       time2 = time.time()
       print '退出'
       print countn
       print 'usetime',time2 - time1
       sys.exit(1)
#dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(10).skip(20)
#dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(20)
#dbs = comment.find({'body':re.compile('不好')})


    for item in dbs:
        if item['userReviewId'] in idList:
            print 'repeat' + item['body'] + item['date'] + item['userReviewId']
            clencomment.remove({'userReviewId':item['userReviewId']})
            clencomment.insert(item)
        else:
        
            #print item['body'] + item['date'] + item['userReviewId'],item.get('isneg')
            if item.get('isneg') == True:
               foranalyse =  item['body'] + item['title']
               foranalyse = foranalyse.replace('\n','')
               foranalyse = foranalyse.lower()
               foranalyse = foranalyse.replace(' ','')
               print foranalyse       
            idList.append(item['userReviewId'])
            countn = countn + 1


print countn
