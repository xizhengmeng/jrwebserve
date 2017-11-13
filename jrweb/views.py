# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse

# from corefunction.coresearch import searchComment
from CoreFunction.CoreSearch import searchComment
# Create your views here.

def test(request):
    return HttpResponse("ceshiceshi")

def searchCommentFunction(request):
    postObj = request.POST()
    getObj = request.GET()

    searchkey = ''
    sorekey = ''
    pageindex = 0
    pagesize = 0

    if type(postObj) != type(None):
       searchkey = request.POST.get('searchkey')
       sorekey = request.POST.get('sorekey')
       pageindex = request.POST.get('pageindex')
       pagesize = request.POST.get('pagesize')
    elif type(getObj) != type(None):
       searchkey = request.GET.get('searchkey')
       sorekey = request.GET.get('sorekey')
       pageindex = request.GET.get('pageindex')
       pagesize = request.GET.get('pagesize')
    else:
       return HttpResponse('no request body')

    searchResultString = searchComment(searchkey,sorekey,pageindex,pagesize)
    
    return HttpResponse(searchResultString)
