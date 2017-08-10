# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response


import dynaform, urllib2, json

from django.template import RequestContext


# Create your views here.

def index(request):
	f = urllib2.urlopen('http://127.0.0.1:5000/templatize')
	json_form = f.read()
	d = json.loads(json_form)
	formEntry = [ { 'name': 'templateName', 'label': 'Template', 'type': 'select', 'choices': [ {'name': k, 'value': k } for k in d['templates']]}]
	json_form = json.dumps(formEntry)
	form_class = dynaform.get_form(json_form)
	data = {}
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			data = form.cleaned_data
	else:
		form = form_class()
	return render_to_response("index.html", { 'form': form, 'data': data}, RequestContext(request))

def template(request):
	data = request.POST.dict()
	if 'templateName' not in data.keys():
		return HttpResponse("Template Check Done")
	templateName = data['templateName']

	f = urllib2.urlopen('http://127.0.0.1:5000/templatize/' + templateName)
	src = f.read()
	data = json.loads(src)
	return render_to_response('templateform.html', context={'templateName': templateName, 'jsonData': src})

def render(request):
	reqData = json.loads(request.body)
	templateName = reqData['templateName']
	config = json.dumps(reqData['params'])
	req = urllib2.Request('http://127.0.0.1:5000/templatize/' + templateName, config, {"Content-Type": 'application/json'})
	f = urllib2.urlopen(req)
	src = f.read()
	print type(src)
	return HttpResponse(src.replace("\\n", "<br>").replace('\"', '', 1))
