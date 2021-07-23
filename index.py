from django.shortcuts import render
from django.template import loader

def first(request):
    return render(request,'first.html',{'name':'hello','hlink':'http://localhost:8000/first'})
def contact(request):
    return render(request,'contact.html',{'name':'hello','hlink':'http://localhost:8000/contact'})
def about(request):
    return render(request,'about.html',{'name':'hello','hlink':'http://localhost:8000/about'})
def location(request):
    return render(request,'location.html',{'name':'hello','hlink':'http://localhost:8000/location'})