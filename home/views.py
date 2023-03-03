from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import requires_csrf_token


def home(request):
    return render(request, 'home.html')

@requires_csrf_token
def mylogout(request):
    logout(request)
    return redirect('home')
# Create your views here.
