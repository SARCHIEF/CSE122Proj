from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def learn(request):
    return render(request,"learn.html")

def develope(request):
    return render(request,"develope.html")

def sell(request):
    return render(request,"sell.html")

def contacts(request):
    return render(request,"contacts.html")