 #-*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba

reload(sys)
sys.setdefaultencoding( "utf-8" )

items = open('../coredata/fordelete.txt').read().split('\n')

itemnews = open('../coredata/neg.txt').read().split('\n')

count = 0
for item in itemnews:
    if item not in items:
       print item
       count = count + 1

print len(itemnews)
print count
print len(items)