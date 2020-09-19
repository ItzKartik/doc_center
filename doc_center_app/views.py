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
import datetime

def save_activity(request, text):
    models.activity.objects.create(user_id=give_u(request.user.username), activity=text)
    return None

def give_u(uname):
    user = User.objects.get(username=uname)
    return user

def check_for_membership(request):
    m = models.type_of_membership.objects.filter(user_id=give_u(request.user.username))
    if m:
        return True
    else:
        return False

def index(request):
    types = models.types.objects.all()
    return render(request, 'index.html', {'types': types})

def membership(request):
    if request.method == 'POST':
        types = models.types.objects.get(type_id=request.POST['type_id'])
        m = models.type_of_membership.objects.filter(user_id=give_u(request.user.username))
        if m:
            m.update(membership_type=types)
        else:
            models.type_of_membership.objects.create(user_id=give_u(request.user.username), membership_type=types)
        activity = 'Applied For Type '+types.type_name
        save_activity(request, activity)
        return redirect('activity')
    else:
        types = models.types.objects.all()
        return render(request, 'homepages/membership.html', {'types': types})

def doc_view(request, pk):
    docs = models.docs.objects.get(doc_id=pk)
    if check_for_membership(request) == True:
        context = {
            'docs': docs,
            'error': None
        }
    else:
        context = {
            'docs': docs,
            'error': 'You Have To Select A Membership Type Before Applying For Bids'
        }
    return render(request, 'homepages/doc_view.html', context)

def upload_docs(request):
    if request.method == 'POST':
        doc_name = request.POST['doc_name']
        docs = models.docs.objects.create(
            user_id=give_u(request.user.username), doc_name=doc_name, doc=request.FILES['document'])
        activity = doc_name+' Uploaded'
        save_activity(request, activity)
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
        if check_for_membership(request) == True:
            context = {
                'docs': docs,
                'error': None
            }
        else:
            context = {
                'docs': docs,
                'error': 'You Have To Select A Membership Type Before Using This Service'
            }
        return render(request, 'homepages/docs.html', context)


def bids(request):
    if request.method == 'POST':
        doc_id = request.POST['doc_id']
        bid_amt = request.POST['bid_amt']
        docs = models.docs.objects.get(doc_id=doc_id)
        bids = models.bids.objects.create(linker=docs, owner=docs.user_id.username, bid_amt=bid_amt)

        activity = 'Bidded On '+docs.doc_name
        save_activity(request, activity)

        bids.save()
        return HttpResponse('Done')
    else:
        bids = models.bids.objects.filter(owner=request.user.username)
        context = {
            'bids': bids
        }
        return render(request, 'homepages/bids.html', context)

def activity(request):
    act = models.activity.objects.filter(user_id=give_u(request.user.username))
    return render(request, 'homepages/activity.html', {'act': act})

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