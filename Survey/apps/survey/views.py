from django.shortcuts import render, HttpResponse, redirect
from django import forms

# Create your views here.
def index(request):
    return render(request, "survey_form/index.html")

def submit(request):
    if request.session.get("count") == None:
        request.session["count"] = 0

    request.session["name"]=request.POST["name"]
    request.session["princess"]=request.POST["princess"]
    request.session["character"]=request.POST["character"]
    request.session["comment"]=request.POST["comment"]
    request.session["count"] += 1
    return render(request,"survey_form/submitted.html")

def result(request):
    return redirect("/")
