from django.shortcuts import render
from . import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.conf import settings
from django.core import serializers
import json
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import re
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import uuid

def give_u(uname):
    user = User.objects.get(username=uname)
    return user

def index(request):
    types = models.types.objects.all()
    return render(request, 'index.html', {'types': types})

def membership(request):
    types = models.types.objects.all()
    return render(request, 'homepages/membership.html', {'types': types})

def upload_docs(request):
    if request.method == 'POST':
        docs = models.docs.objects.create(
            user_id=give_u(request.user.username), doc_name=request.POST['doc_name'], doc=request.POST['document'])
        return redirect('docs')

def docs(request):
    if request.method == 'POST':
        user = request.user.username
        u = User.objects.get(username=user)
        docs = models.docs.objects.filter(user_id=u)
        d = serializers.serialize('json', docs)
        return HttpResponse(d, content_type="application/json")
    else:
        docs = models.docs.objects.all()
        return render(request, 'homepages/docs.html', {'docs': docs})

def getin(request):
    if request.method == 'POST':
        id_password = request.POST['pass']
        id_email = request.POST['mail']

        e_mail = User.objects.filter(email=id_email)
        username = id_email.split('@')
        if e_mail:
            user = authenticate(request, username=username[0], password=id_password)
            login(request, user)
            if login:
                return HttpResponse('done')
        else:
            user = User.objects.create(username=username[0], email=id_email, password=id_password)
            user.set_password(id_password)
            user.save()
            login(request, user)
            return HttpResponse('done')
    else:
        return render(request, 'getin.html')

def logout_view(request):
    logout(request)
    return redirect('getin')