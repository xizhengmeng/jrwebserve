# -*- coding: utf-8 -*-

import os, time, json ,sys
from pymongo import MongoClient
import re
import logging
import datetime
#
logger = logging.getLogger('sourceDns.webdns.views')

reload(sys)
sys.setdefaultencoding("utf-8")

connection = MongoClient("localhost", 27017)
mydb = connection.Spider  # new a database
comment = mydb.Comment  # new a table
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

    dbs = clencomment.find({'forsearch': re.compile(searchkey)}).sort([('date',-1)]).limit(pagesize).skip(skipnumber)

    list = []
    for item in dbs:
        dic = {}
        dic['evaluateId'] = item.get('userReviewId')
        dic['content'] = item.get('body')
        dic['time'] = item.get('date')
        dic['userName'] = item.get('name')
        dic['score'] = item.get('rating')
        dic['title'] = item.get('title')
        logger.info(dic['title'])
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

def getcommentbaseinfo():
    allcomment = comment.find({})
    cleancomment = clencomment.find({})

    allcount = allcomment.count()
    clencount = clencomment.count()

    negcomment = clencomment.find({'isneg':True})
    negcount = negcomment.count()

    poscount = clencount - negcount

    now_time = datetime.datetime.now()
    now_time_string = now_time.strftime('%Y-%m-%d')
    yes_time = now_time + datetime.timedelta(days=-30)
    yes_time_nyr = yes_time.strftime('%Y-%m-%d')

    dbs = clencomment.find({"date": {"$gte": yes_time_nyr, "$lt": now_time_string}})

    returnList = []

    timedic = {}
    for item in dbs:
        time = item.get('date')
        timeitem = timedic.get(time)
        if type(timeitem) == type(None):
            timeitem = {}
            timedic[time] = timeitem
            isneg = item.get('isneg')
            if isneg:
                timeitem['negcount'] = 1
            else:
                timeitem['poscount'] = 1
        else:
            isneg = item.get('isneg')
            if isneg:
                negcount = timeitem.get('negcount')
                if type(negcount) == type(None):
                    negcount = 1
                else:
                    negcount = negcount + 1
                timeitem['negcount'] = negcount
            else:
                poscount = timeitem.get('poscount')
                if type(poscount) == type(None):
                    poscount = 1
                else:
                    poscount = poscount + 1
                timeitem['poscount'] = poscount

    keys = timedic.keys()
    logger.info(keys)
    logger.info(timedic)
    for key in keys:
        countItem = timedic.get(key)
        poscount = countItem.get('poscount')
        negcount = countItem.get('negcount')

        if type(poscount) == type(None):
            poscount = 0

        if type(negcount) == type(None):
            negcount = 0

        itemDic = {}
        itemDic['time'] = key
        itemDic['poscount'] = poscount
        itemDic['negcount'] = negcount

        returnList.append(itemDic)

    returnDic = {}
    returnDic['allcount'] = allcount
    returnDic['clencount'] = clencount
    returnDic['negcount'] = negcount
    returnDic['poscount'] = poscount
    returnDic['commentlist'] = returnList

    resultString = json.dumps(returnDic)

    return resultString