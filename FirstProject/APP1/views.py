from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f11(request):
    return HttpResponse("<h2><center>Hello, Good morning user...!! have a nice day...</center></h2><hr/>");
    
