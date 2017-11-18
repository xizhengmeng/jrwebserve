 #-*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba

reload(sys)
sys.setdefaultencoding( "utf-8" )

items = open('../coredata/fordelete.txt').read().split('\n')

print len(items)

itemnews = open('../coredata/neg.txt').read().split('\r')

for item in itemnews:
    if item not in items:
       print item