#!/usr/bin/env python
# coding:utf-8
import os,sys,jieba,time,re,datetime
from pymongo import MongoClient
from numpy import *


#1.将A库移动到B库
#2.去重
#3.分析数据
#4.查询数据
#5.词频排序
#6.插入查询分词

reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = MongoClient("localhost",27017)
mydb = connection.Spider # new a database
comment = mydb.Comment # new a table
clencomment = mydb.CleanComment

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
        return True

    else:
        return False


def movedatafrommongotocleanmogo():#move mongodata

    cdbs = clencomment.find({})
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
              item['forsearch'] = forsearch
              clencomment.save(item)
              idList.append(item['userReviewId'])


def analysesentence():
    time1 = time.time()

    neglist = open('../coredata/neg.txt').read().split('\n')
    poslist = open('../coredata/pos.txt').read().split('\r')
    neulist = []

    abpost = ['非常满意', '强烈好评', '值得信赖的京东', '京东支持', '感谢', '谢谢', '支持京东', '强哥', '给你好评', '放心的京东', '会一直支持的', '会支持的', '信赖京东',
              '京东越来越好']
    jieba.load_userdict('../coredata/customdict.txt')

    count = 0

    for i in range(20):
        dbs = clencomment.find({}).limit(1000).skip(i * 1000)
        analyseList = []
        if dbs.count(True) == 0:
            time2 = time.time()
            print '退出'
            print count
            print 'usetime', time2 - time1
            sys.exit(1)
        for item in dbs:
            if item.get('hasanalyse') == True:
                continue

            nominal = 0
            forsearch = item.get('forsearch')
            if type(forsearch) == type(None):
                continue
            count = count + 1
            isAbsuPos = False
            for setence in abpost:
                if setence in forsearch:
                    print 'abpos' + forsearch
                    isAbsuPos = True

            if isAbsuPos:
                item['hasanalyse'] = True
                item['isneg'] = False
                clencomment.remove({'userReviewId': item['userReviewId']})
                clencomment.insert(item)
                continue

            seg_list = jieba.cut(forsearch)

            seg_listnew = []

            for seg in seg_list:
                seg_listnew.append(seg)

            for word in seg_listnew:
                if word in poslist:
                    # print '1'+word
                    pass
                elif word in neglist:
                    lastindex = seg_listnew.index(word) - 1
                    if lastindex >= 0:
                        lastitem = seg_listnew[lastindex]
                        print 'last' + lastitem
                        if lastitem == '无' or lastitem == '不' or lastitem == '没有' or lastitem == '非' or lastitem == '不是':
                            print 'fei' + lastitem + word
                        else:
                            print '2' + word
                            nominal = nominal - 1
                    else:
                        nominal = nominal - 1
                else:
                    # print '3'+word
                    pass
            item['hasanalyse'] = True
            item['nominal'] = '%d' % nominal
            if nominal < 0:
                item['isneg'] = True
            else:
                item['isneg'] = False
            clencomment.remove({'userReviewId': item['userReviewId']})
            clencomment.insert(item)
            if nominal != 0:
                print 'neg', item['isneg'], item['forsearch']


def findalldata():
    time1 = time.time()
    idList = []
    countn = 0
    for i in range(1):
        dbs = clencomment.find({}).limit(1000).skip(i * 1000)

        now_time = datetime.datetime.now()
        now_time_string = now_time.strftime('%Y-%m-%d')
        yes_time = now_time + datetime.timedelta(days=-10)
        yes_time_nyr = yes_time.strftime('%Y-%m-%d')

        print now_time_string, yes_time_nyr

        dbs = clencomment.find({"date": {"$gte": yes_time_nyr, "$lt": now_time_string}})

        print 'count', dbs.count, i * 1000
        if dbs.count(True) == 0:
            time2 = time.time()
            print '退出'
            print countn
            print 'usetime', time2 - time1
            sys.exit(1)
            # dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(10).skip(20)
            # dbs = comment.find({'body':re.compile('白条')}).sort([('date',1)]).limit(20)
            # dbs = comment.find({'body':re.compile('不好')})

        for item in dbs:
            if item['userReviewId'] in idList:
                print 'repeat' + item['body'] + item['date'] + item['userReviewId']
                clencomment.remove({'userReviewId': item['userReviewId']})
                clencomment.insert(item)
            else:
                print item['body'] + item['date'] + item['userReviewId'], item.get('isneg')
                idList.append(item['userReviewId'])
                countn = countn + 1

    print countn


def frequencyalldata():
    cleanall = clencomment.find({})
    keyword = {}
    for item in cleanall:
        body = item['body']
        seg_list = seg_list = jieba.cut(body)
        for word in seg_list:
            count = keyword.get(word)
        if type(count) == type(None):
            count = 1
            keyword[word] = count
        else:
            count = count + 1
            keyword[word] = count

    resultDict = sorted(keyword.items(), key=lambda d: d[1], reverse=True)

    for item in resultDict:
        print item[0], item[1]


def loadDataSet():
    jieba.load_userdict('customdict.txt')

    postingList = []
    classVec = []

    neglist = open('neg.txt').read().split('\n')
    poslist = open('pos.txt').read().split('\n')

    for line in neglist:
        seg_list = jieba.cut(line)
        seg_listnew = []
        for seg in seg_list:
            seg_listnew.append(seg)
        postingList.append(seg_listnew)
        classVec.append(1)

    for line in poslist:
        seg_list = jieba.cut(line)
        seg_listnew = []
        for seg in seg_list:
            seg_listnew.append(seg)
        postingList.append(seg_listnew)
        classVec.append(0)

    return postingList, classVec


def createVocabList(dataSet):
    vocabSet = set([])  # create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # union of the two sets
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords);
    p1Num = ones(numWords)  # change to ones()
    p0Denom = 2.0;
    p1Denom = 2.0  # change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)  # change to log()
    p0Vect = log(p0Num / p0Denom)  # change to log()
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    # testEntry = ['love', 'my', 'dalmation']

    testline = '我他妈的是爱你的'

    seg_list = jieba.cut(testline)

    seg_listnew = []
    for item in seg_list:
        seg_listnew.append(item)

    testEntry = seg_listnew

    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)