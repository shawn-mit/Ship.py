from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404


def index(request):
    template_name = 'piechart.html'
    return render(request, template_name, {})
