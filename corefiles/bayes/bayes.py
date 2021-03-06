# -*- coding: utf-8 -*-
'''
Created on Oct 19, 2010

@author: Peter
'''
from numpy import *
import jieba,sys
import numpy,re

reload(sys)
sys.setdefaultencoding( "utf-8" )

abpath = sys.path[0] + '/'
if 'bayes/' not in abpath:
	abpath = abpath+'bayes/'
jieba.load_userdict(abpath+'customdict.txt')

stopwords = open(abpath+'stopwords.txt','r').read().split('\n')

def translate(str):
    str = str.replace(',','')
    str = str.replace('。','')
    str = str.replace('！','')
    str = str.replace('!','')
    line = str.strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等
    p2 = re.compile(ur'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    zh = " ".join(p2.split(line)).strip()
    zh = ",".join(zh.split())
    outStr = zh  # 经过相关处理后得到中文的文本
    return outStr

def loadDataEnglishSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def loadDataSet():

    # abpath = sys.path[0] + '/'
    # jieba.load_userdict(abpath+'customdict.txt')

    postingList = []
    classVec = []

    neglist = open(abpath+'neg.txt').read().split('\n')
    poslist = open(abpath+'pos.txt').read().split('\n')

    for line in neglist:
        newline = translate(line)
        seg_list = jieba.cut(newline)
        seg_listnew = []
        for seg in seg_list:
            if seg not in stopwords:
               seg_listnew.append(seg)
        postingList.append(seg_listnew)
        classVec.append(1)

    for line in poslist:
        newline = translate(line)
        seg_list = jieba.cut(newline)
        seg_listnew = []
        for seg in seg_list:
            if seg not in stopwords:
               seg_listnew.append(seg)
        postingList.append(seg_listnew)
        classVec.append(0) 
        
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    isnotintVoc = []
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
        # else: print "the word: %s is not in my Vocabulary!" % word
        else:
            isnotintVoc.append(word)

    if len(isnotintVoc) != 0:
       # print 'isnotIn',''.join(isnotintVoc)
       print 'isnotIn','/'.join(isnotintVoc),'*******',''.join(inputSet)
    return returnVec

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)     #change to ones() 
    p0Denom = 2.0; p1Denom = 2.0                        #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def numberOfcanotUse(vocabList, inputSet):
    count = 0
    for word in inputSet:
        if word not in vocabList:
           count = count + 1
    return count

def isUseful(content):
    myVocabList = numpy.load(abpath + "t.npy").tolist()
    newline = translate(content)
    seg_list = jieba.cut(newline)
    seg_listnew = []
    for seg in seg_list:
        if seg not in stopwords:
           seg_listnew.append(seg)

    count = numberOfcanotUse(myVocabList,seg_listnew)
    if count >= 3:
        return False
    else:
        return True

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))

    numpy.save(abpath+"t.npy", myVocabList)
    numpy.save(abpath+"a.npy", p0V)
    numpy.save(abpath+"b.npy", p1V)
    numpy.save(abpath+"c.npy", pAb)

     
    # testEntry = ['love', 'my', 'dalmation']
    # testline = '京东还是不错'

    # seg_list = jieba.cut(testline)

    # seg_listnew = []
    # for item in seg_list:
    #     seg_listnew.append(item)

    # testEntry = seg_listnew

    # thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    # print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)

def testModel(string):
    # testline = 'ipad看不到qq合作登陆，登陆不了，望修复ipad看不到qq合作登陆，登陆不了，望修复'

    testline = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，！。？、~@#￥%……&*（）]+",'',string)
    testline = testline.replace('！','')
    testline = testline.replace('，','')
    testline = testline.replace('。','')

    seg_list = jieba.cut(testline)

    seg_listnew = []
    for item in seg_list:
        if item not in stopwords:
               seg_listnew.append(item)

    testEntry = seg_listnew

    myVocabList = numpy.load(abpath + "t.npy").tolist()
    p0V = numpy.load(abpath + "a.npy")
    p1V = numpy.load(abpath + "b.npy")
    pAb = numpy.load(abpath + "c.npy")

    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    # print string,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
    return classifyNB(thisDoc,p0V,p1V,pAb)

def textParse(bigString):    #input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2] 
    
def spamTest():
    docList=[]; classList = []; fullText =[]
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)#create vocabulary
    trainingSet = range(50); testSet=[]           #create test set
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error",docList[docIndex]
    print 'the error rate is: ',float(errorCount)/len(testSet)
    #return vocabList,fullText

def calcMostFreq(vocabList,fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True) 
    return sortedFreq[:30]       

def localWords(feed1,feed0):
    import feedparser
    docList=[]; classList = []; fullText =[]
    minLen = min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1) #NY is class 1
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)#create vocabulary
    top30Words = calcMostFreq(vocabList,fullText)   #remove top 30 words
    for pairW in top30Words:
        if pairW[0] in vocabList: vocabList.remove(pairW[0])
    trainingSet = range(2*minLen); testSet=[]           #create test set
    for i in range(20):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ',float(errorCount)/len(testSet)
    return vocabList,p0V,p1V

def getTopWords(ny,sf):
    import operator
    vocabList,p0V,p1V=localWords(ny,sf)
    topNY=[]; topSF=[]
    for i in range(len(p0V)):
        if p0V[i] > -6.0 : topSF.append((vocabList[i],p0V[i]))
        if p1V[i] > -6.0 : topNY.append((vocabList[i],p1V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"
    for item in sortedNY:
        print item[0]
