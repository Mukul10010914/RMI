from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from product.models import *
from Client.models import *
import random

def home(request):
	i = product.objects.all()
	r = review.objects.all()
	t = list(i)
	products = {}

	s = random.sample(t, 4)

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)
		
	return render(request, "home.html", {'pro':products, 's':s, 'r':r})

def about(request):
	i = product.objects.all()
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)
		
	return render(request, "about.html", {'pro':products})

def contact(request):
	i = product.objects.all()
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)
		
	return render(request, "contact.html", {'pro':products})