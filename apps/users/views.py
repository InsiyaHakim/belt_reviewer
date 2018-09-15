# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from ..authors.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'users/index.html')

def creating_user(request):
    if request.method == 'POST':
        error=User.object.creating_db(request.POST)
        if len(error)>0:
            for err in error:
                messages.error(request, err)
            return redirect("user:index")
        else:
            print "created"
            return redirect("user:index")
    else:
        return redirect("user:index")

def log(request):
    if request.method == "POST":
        error=User.object.loging(request.POST)
        if type(error) == list:
            for err in error:
                messages.error(request, err)
            return redirect("user:index")
        else:
            user_id= str(error)
            if "user_id" not in request.session:
                request.session['user_id']=user_id
            user=User.object.selecting_user(user_id)
            context={
                "user":user
            }
            return render(request,"users/login.html",context)
    else:
        if 'user_id' in request.session:
            user_id=request.session['user_id']
            user = User.object.selecting_user(user_id)[0]
            context = {
                "user": user
            }
            return render(request, "users/login.html", context)
        else:
            return redirect("user:index")

def logout(request):
    if request.method == "POST":
        request.session.clear()
        return redirect("user:index")
    else:
        if 'user_id' in request.session:
            user_id=request.session['user_id']
            user = User.object.selecting_user(user_id)
            context = {
                "user": user
            }
            return render(request, "users/login.html", context)
        else:
            return redirect("user:index")

def author(request):
    if "user_id" in request.session:
        authors=User.object.selecting_all_authors()
        context={
            "authors":authors
        }
        context['n'] = range(1, 6)
        return render(request,"users/author.html",context)
    else:
        return redirect("user:index")

def author_creating(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        error=User.object.author_creating(request.POST,user_id)
        if type(error)== list:
            for err in error:
                messages.error(request, err)
            return redirect("user:author")
        else:
            print error
            return redirect("user:author")
    else:
        return redirect("user:index")
