# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response


import urllib2, json,ConfigParser, subprocess

from django.template import RequestContext


# Create your views here.

def template(request):
	cfg = ConfigParser.ConfigParser()
	cfg.read('/app/etc/netconfig.ini')
	f = urllib2.urlopen('http://' + cfg.get('backend', 'ip') + ':' + cfg.get('backend', 'port') + '/templatize')
	src = f.read()
	data = json.loads(src)
	tgtData = [ str(k) for k in data['templates'] ]
	localaddr = cfg.get('frontend', 'ip')
	return render_to_response('templateform.html', context={'jsonData': tgtData, 'localaddr': localaddr})

def render(request):
	cfg = ConfigParser.ConfigParser()
	cfg.read('/app/etc/netconfig.ini')
	reqData = json.loads(request.body)
	templateName = reqData['templateName']
	config = json.dumps(reqData['params'])
	req = urllib2.Request('http://' + cfg.get('backend', 'ip') + ':' + cfg.get('backend', 'port') + '/templatize/' + templateName, config, {"Content-Type": 'application/json'})
	f = urllib2.urlopen(req)
	src = f.read()
	print type(src)
	return HttpResponse(src.replace("\\n", "<br>").replace('\"', '', 1))

def getTemplate(request):
	cfg = ConfigParser.ConfigParser()
	cfg.read('/app/etc/netconfig.ini')
	reqData = json.loads(request.body)
	templateName = reqData['templateName']
	print templateName
	f = urllib2.urlopen('http://' + cfg.get('backend', 'ip') + ':' + cfg.get('backend', 'port') + '/templatize/' + templateName)
	src = f.read()
	data = json.loads(src)
	return JsonResponse(data)
