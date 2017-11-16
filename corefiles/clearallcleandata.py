#!/usr/bin/env python
# coding:utf-8

import os,sys
import pymongo
import re

reload(sys)
sys.setdefaultencoding( "utf-8" )

connection = pymongo.MongoClient("localhost",27017)
mydb = connection.Spider # new a database
clencomment = mydb.CleanComment

clencomment.remove({})