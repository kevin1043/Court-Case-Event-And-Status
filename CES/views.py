from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


def home(request):
    my_dict = {'insert_home': "", }
    return render(request, 'home.html', context=my_dict)
# Create your views here.
