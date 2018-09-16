# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..authors.models import *
from ..users.models import User

# Create your models here.

class BookManager(models.Manager):
    def book_record(self):
        pass



class Book(models.Model):
    title=models.CharField(max_length=255)
    user_id=models.ForeignKey(User,related_name="user_id")
    author_id=models.ForeignKey(Authors,related_name="author_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object=BookManager()
