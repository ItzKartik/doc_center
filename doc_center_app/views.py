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

def index(request):
    types = models.types.objects.all()
    return render(request, 'index.html', {'types': types})

def getin(request):
    if request.method == 'POST':
        id_password = request.POST['pass']
        id_email = request.POST['mail']

        e_mail = User.objects.filter(email=id_email)
        if e_mail:
            user = authenticate(request, email=id_email, password=id_password)
            login(request, user)
            return HttpResponse('done')
        else:
            username = id_email.split('@')
            user = User.objects.create(username=username[0], email=id_email, password=id_password)
            user.set_password(id_password)
            user.save()
            login(request, user)
            return HttpResponse('done')
    else:
        return render(request, 'getin.html')

def logout_view(request):
    logout(request)
    return redirect('index')