# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse

# from corefunction.coresearch import searchComment
from CoreFunction.CoreSearch import searchComment,createKeyWordList,getcommentbaseinfo
# Create your views here.
import logging
#

logger = logging.getLogger('sourceDns.webdns.views')

def test(request):
    return HttpResponse("ceshiceshi")

def searchCommentFunction(request):

    searchkey = ''
    sorekey = ''
    pageindex = 0
    pagesize = 0

    if request.method == 'POST':
       logger.info('POST')
       searchkey = request.POST.get('searchkey')
       sorekey = request.POST.get('sorekey')
       pageindex = request.POST.get('pageindex')
       pagesize = request.POST.get('pagesize')
       lastesttime = request.POST.get('lastesttime')
       isneg = request.POST.get('isneg')
       logger.info(request.POST.copy())
       logger.info(request.body)
       logger.info({'searchkey':searchkey,'soreky':sorekey,'pageindex':pageindex,'pagesize':pagesize})
    elif request.method == 'GET':
       logger.info('GET')
       searchkey = request.GET.get('searchkey')
       sorekey = request.GET.get('sorekey')
       pageindex = request.GET.get('pageindex')
       pagesize = request.GET.get('pagesize')
       lastesttime = request.GET.get('lastesttime')
       isneg = request.GET.get('isneg')
       logger.info(request.GET.copy())
       logger.info({'searchkey': searchkey, 'soreky': sorekey, 'pageindex': pageindex, 'pagesize': pagesize,'lastesttime': lastesttime,'isneg':isneg})
    else:
       return HttpResponse('no request body')

    searchResultString = searchComment(searchkey,sorekey,pageindex,pagesize,lastesttime,isneg)
    return HttpResponse(searchResultString)

def getKeyWordFunction(request):
    returnString = createKeyWordList()
    return HttpResponse(returnString)


def getBaseInfoFunction(request):
    returnString = getcommentbaseinfo()
    return HttpResponse(returnString)
