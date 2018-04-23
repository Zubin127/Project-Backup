from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

##--NormalUser/--##
def index(request):
    return render(request,'Normal_User/index.html')

def register(request):
    return render(request,'Normal_User/register.html')
