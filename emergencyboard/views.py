from django.shortcuts import render, redirect
from . import helper


def home(request):
    return render(request, 'emergencyboard/home.html')


def random_link(request):
    random_link = helper.get_random_link()
    return redirect(random_link)
