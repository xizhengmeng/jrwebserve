# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class TutorialPipeline(object):

    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄
        self.singleset = set()
        dbs = self.coll.find({})
        for item in dbs:
            userReviewId = item['userReviewId']
            self.singleset.add(userReviewId)

    def process_item(self, item, spider):
        if spider.name == 'ios':
           print 'ios'
           # print item['body']
           # print item['date']
           userReviewId = item['userReviewId']
           if userReviewId in self.singleset:
              raise DropItem("Duplicate item found: %s" % item)
           else:
              item['storename'] = 'iosappstore'
              print item['body']
              postItem = dict(item)  # 把item转化成字典形式
              self.coll.insert(postItem)  # 向数据库插入一条记录
        elif spider.name == 'andorid':
            print 'andorid'
            userReviewId = item['userReviewId']
            if userReviewId in self.singleset:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                item['storename'] = 'android1'
                postItem = dict(item)  # 把item转化成字典形式
                self.coll.insert(postItem)  # 向数据库插入一条记录

        return item
