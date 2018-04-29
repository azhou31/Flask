from django.shortcuts import render, HttpResponse, redirect
from time import strftime
from datetime import datetime
import pytz
from tzlocal import get_localzone
import time

# Create your views here.
def index(request):
    # context ={
    #     "time":strftime("%m-%d-%Y %H:%M %p")
    # }
    FORMAT = '%Y-%m-%dT%H:%M:%S%Z'
    date=datetime.strptime(time.strftime(FORMAT, time.localtime()),FORMAT)
    context = {
        # "time": datetime.now().replace(tzinfo=pytz.utc)
        "time":date
    }
    return render(request,'timedisplay/index.html', context)