# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response


import urllib2, json

from django.template import RequestContext


# Create your views here.

def template(request):
	f = urllib2.urlopen('http://127.0.0.1:5000/templatize')
	src = f.read()
	data = json.loads(src)
	tgtData = [ str(k) for k in data['templates'] ]
	return render_to_response('templateform.html', context={'jsonData': tgtData})

def render(request):
	reqData = json.loads(request.body)
	templateName = reqData['templateName']
	config = json.dumps(reqData['params'])
	req = urllib2.Request('http://127.0.0.1:5000/templatize/' + templateName, config, {"Content-Type": 'application/json'})
	f = urllib2.urlopen(req)
	src = f.read()
	print type(src)
	return HttpResponse(src.replace("\\n", "<br>")[1:-2])
#	return HttpResponse(src.replace("\\n", "\\r\\n").replace('\"', '', 1))
#	return HttpResponse(src.replace('\"', '', 1))

def getTemplate(request):
	reqData = json.loads(request.body)
	templateName = reqData['templateName']
	print templateName
	f = urllib2.urlopen('http://127.0.0.1:5000/templatize/' + templateName)
	src = f.read()
	data = json.loads(src)
	return JsonResponse(data)
