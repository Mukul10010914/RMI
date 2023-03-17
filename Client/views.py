from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from .models import *
from product.models import *
import random

def enqueryy(request):
	i = product.objects.order_by('cat')
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	if request.method == "POST":
		coname = request.POST.get('coname')
		pname = request.POST.get('pname')
		email = request.POST.get('email')
		number = request.POST.get('number')
		desc = request.POST.get('desc')

		q = enquery(coname=coname, pname=pname, email=email, number=number, desc=desc)
		q.save()
		return render(request, "thank.html", {})

	else:
		return render(request, "enquery.html", {'pro':products})

def reviews(request):
	i = product.objects.order_by('cat')
	products = {}

	for it in i:
		key = it.cat.name
		products.setdefault(key, []).append(it)

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		rate = request.POST.get('rate')
		feed = request.POST.get('feed')

		r = review(name=name, email=email, comment=feed, rate=rate)
		r.save()

		return render(request, "thank.html", {})

	else:
		return render(request, "review_form.html", {'pro':products})