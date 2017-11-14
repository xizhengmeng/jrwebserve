#!/usr/bin/env python
# coding:utf-8

import time
import os

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

while True:
    os.chdir('/root/jdjr/spider')
    os.system("scrapy crawl spider")
    time.sleep(21600)  #每隔一天运行一次 6*60*60=21600s
