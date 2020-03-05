from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    return HttpResponse("You are at the index.")


def detail(request, User_id):
    return HttpResponse("You are looking at User %s." % User_id)