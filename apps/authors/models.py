# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AuthorsManagaer(models.Manager):
    def author_record(self):
        pass

class Authors(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    object=AuthorsManagaer()