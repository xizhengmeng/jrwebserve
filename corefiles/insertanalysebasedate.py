# -*- coding: utf-8 -*- 
import xdrlib ,sys
import xlrd
from pymongo import MongoClient

connection = MongoClient("localhost", 27017)
mydb = connection.Spider  # new a database
basedata = mydb.analysebasedata  # new a table

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file,colnameindex,by_index):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    # ncols = table.ncols #列数
    # colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             # app = {}
             # for i in range(len(colnames)):
             #    app[colnames[i]] = row[i]
             list.append(row[0])
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main():

   # dbs = basedata.find({})
   # for item in dbs:
   #     print item
   # sys.exit(1)

   negtables = excel_table_byindex('../coredata/analysebasedata.xlsx', 0, 0)

   postables = excel_table_byindex('../coredata/analysebasedata.xlsx', 0, 1)

   neutables = excel_table_byindex('../coredata/analysebasedata.xlsx', 0, 2)

   wordDic = {}
   neglist = []
   poslist = []
   neulist = []

   for row in negtables:
       neglist.append(row)

   for row in postables:
       poslist.append(row)

   for row in neutables:
       neulist.append(row)

   print len(neutables)
   wordDic['pos'] = poslist
   wordDic['neg'] = neglist
   wordDic['neu'] = neulist
   wordDic['name'] = 'word'

   basedata.remove({})
   basedata.insert(wordDic)

if __name__=="__main__":
    main()