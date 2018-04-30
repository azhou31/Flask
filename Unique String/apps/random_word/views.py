from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if request.session.get('count') == None:
        request.session["count"] = 0
    return render(request,"randomword/index.html")

def generate(request):
    request.session["count"] += 1
    request.session["rand_word"] = get_random_string(length=14)
    return redirect("/")

def reset(request):
    request.session["count"] = 0
    return redirect("/")