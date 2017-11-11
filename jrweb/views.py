# -*- coding: utf-8 -*-
import os,datetime,json
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
    return HttpResponse("ceshiceshi")