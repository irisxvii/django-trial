from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_print(request):
    return HttpResponse("<b>i love you 3000")
