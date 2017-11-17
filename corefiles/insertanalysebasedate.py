# -*- coding: utf-8 -*- 
# import xdrlib ,sys
# import xlrd
from pymongo import MongoClient

connection = MongoClient("localhost", 27017)
mydb = connection.database  # new a database
basedata = mydb.analysebasedata  # new a table

# def open_excel(file):
#     try:
#         data = xlrd.open_workbook(file)
#         return data
#     except Exception,e:
#         print str(e)
# #根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
# def excel_table_byindex(file,colnameindex,by_index):
#     data = open_excel(file)
#     table = data.sheets()[by_index]
#     nrows = table.nrows #行数
#     # ncols = table.ncols #列数
#     # colnames =  table.row_values(colnameindex) #某一行数据
#     list =[]
#     for rownum in range(1,nrows):
#          row = table.row_values(rownum)
#          if row:
#              # app = {}
#              # for i in range(len(colnames)):
#              #    app[colnames[i]] = row[i]
#              list.append(row[0])
#     return list
#
# #根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
# def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
#     data = open_excel(file)
#     table = data.sheet_by_name(by_name)
#     nrows = table.nrows #行数
#     colnames =  table.row_values(colnameindex) #某一行数据
#     list =[]
#     for rownum in range(1,nrows):
#          row = table.row_values(rownum)
#          if row:
#              app = {}
#              for i in range(len(colnames)):
#                 app[colnames[i]] = row[i]
#              list.append(app)
#     return list



# dbs = basedata.find({})
# for item in dbs:
#     print item
# sys.exit(1)
wordDic = {}

for i in range(3):
   if i == 0:
      tables = open('../coredata/neg.txt').read().split('\r')
      wordDic['neg'] = tables
   elif i == 1:
      tables = open('../coredata/pos.txt').read().split('\r')
      wordDic['pos'] = tables
   elif i == 2:
      tables = open('../coredata/neu.txt').read().split('\r')
      wordDic['neu'] = tables

basedata.remove({})
basedata.insert(wordDic)