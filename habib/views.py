from django.http import HttpResponse
from django.shortcuts import render

def habib(request):
    return render(request,'habib.html' )