from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    latest_user_list = User.objects.order_by('-name')[:3]
    output = ', '.join([n.name for n in latest_user_list])
    return HttpResponse(output)


def detail(request, User_id):
    return HttpResponse("You are looking at User %s." % User_id)