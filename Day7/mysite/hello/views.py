from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    temp=loader.get_template('grid2.html')
    return HttpResponse(temp.render())
