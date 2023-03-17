from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from .models import *
import random

def view(request):
	i = product.objects.order_by('cat')
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	return render(request, "aproduct.html", {'pro':products})

def desc(request):
	i = product.objects.order_by('cat')
	l = product.objects.all()
	products = {}
	l = list(l)
	s = random.sample(l, 4)

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	if request.method == "POST":
		pname = request.POST.get('pname')
		a = product.objects.get(name=pname)

		return render(request, "desc.html", {'a':a, 'pro':products, 's':s})

	else:
		return redirect('/Product/All/')

def search(request):
	p = request.POST.get('prname')
	o = product.objects.all()
	
	i = o.filter(name__icontains=p)
	t1 = list(i)

	products = {}
	s = {}

	i1 = list(o)

	for it in i1:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	for it in t1:
		key = it.cat.name
		s.setdefault(key, []).append(it)
	

	return render(request, "search.html", {'s':s, 'pro':products, 'prname':p})