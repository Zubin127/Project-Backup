from django.shortcuts import render

def index(request):
    return render(request, 'BusinessUser/index.html', {'title': 'Sign in & Sign up'})
