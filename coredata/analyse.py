 #-*- coding: utf-8 -*-
import os ,sys
from pymongo import MongoClient
import jieba

reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = MongoClient("localhost", 27017)
mydb = connection.database  # new a database
basedata = mydb.analysebasedata  # new a table

mydbs = connection.Spider  # new a database
clencomment = mydbs.CleanComment

basedata = mydb.analysebasedata  # new a table

basedbs = basedata.find({})

neglist = []
poslist = []
neulist = []

for item in basedbs:
    poslist = item['pos']
    neglist = item['neg']
