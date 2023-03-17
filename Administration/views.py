from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings
from .forms import add
from product.models import *
from Client.models import *

def login(request):
	i = product.objects.all()
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	if request.user.is_authenticated:	
		return redirect('/Administration/Home/')

	else:
		u = request.POST.get('username')
		p = request.POST.get('pass')

		user = auth.authenticate(username=u,password=p)

		if user is not None:
			auth.login(request, user)
			return redirect('/Administration/Login/')

		else:
			return render(request, "admin_login.html", {'pro':products})


def add_product(request):
	if request.user.is_superuser:
		i = product.objects.all()
		products = {}

		for it in i:
			key = it.cat.name
			products.setdefault(key, []).append(it)

		form = add()
		return render(request, "add_product.html", {'form':form, 'pro':products})

	else:
		return redirect('/Administration/Login/')

def add_item(request):
	form = add(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		return redirect('/Administration/Add Product/')
	else:
		messages.info(request,'INVALID CREDENTIALS')
		return render(request, "error.html", {'messages':messages})

def ahome(request):
	i = product.objects.all()
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	return render(request, "admin_home.html", {'pro':products})

def logout(request):
	auth.logout(request)
	return redirect('/')

def add_cat(request):
	cname = request.POST.get('cname')

	c = category(name=cname)
	c.save()
	return redirect('/Administration/Add Product')


def enqueries(request):
	i = product.objects.all()
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	if request.user.is_authenticated:
		e = enquery.objects.all()
		return render(request, "view_enquery.html", {'e':e, 'pro':products})

	else:
		return redirect('/Administration/Login/')

def vreviews(request):
	i = product.objects.all()
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	r = review.objects.all()
	return render(request, "view_review.html", {'r':r, 'pro':products})