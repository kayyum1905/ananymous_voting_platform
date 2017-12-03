from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .models import User


def dashboard(request):
    return render(request, 'user/dashboard.html')
