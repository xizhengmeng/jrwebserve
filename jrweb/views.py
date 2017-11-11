# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os,datetime,json
from django.http import HttpResponse
from django.shortcuts import render
from CoreFoundation.Coresearch import searchComment

# Create your views here.

def test(request):
    return HttpResponse("ceshiceshi")

def searchCommentFunction(request):
    # searchkey = request.POST.get('searchkey')
    # sorekey = request.POST.get('sorekey')
    # pageindex = request.POST.get('pageindex')
    # pagesize = request.POST.get('pagesize')

    searchkey = request.GET.get('searchkey')
    sorekey = request.GET.get('sorekey')
    pageindex = request.GET.get('pageindex')
    pagesize = request.GET.get('pagesize')

    searchResultString = searchComment(searchkey,sorekey,pageindex,pagesize)
    
    return HttpResponse(searchResultString)
