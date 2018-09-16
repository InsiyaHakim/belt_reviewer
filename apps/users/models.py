# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..authors.models import *
from ..books.models import *

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

# Create your models here.

class UserManager(models.Manager):

    def creating_db(self,form_data):

        name=str(form_data['name'])
        alias=str(form_data['alias'])
        email=str(form_data['email'])
        password=str(form_data['password'])
        c_password=str(form_data['confirm'])


        error=[]
        if str.isalpha(name) == False or str.isalpha(alias) == False:
            error.append("Name and Alias shouldn't have any digit(s)")
        if len(name) < 2:
            error.append("Name must be atleast 8 character(s)")
        if len(alias) < 2:
            error.append("Alias should be atleast 3 character(s)")
        if not EMAIL_REGEX.match(email):
            error.append("Invalid Email Typed")
        if len(password) < 2:
            error.append("Password must be 8 character(s)")
        if c_password != password:
            error.append("Confirm Password again!!")

        check_email=self.filter(email=email)
        if len(check_email)!= 0:
            error.append("Invalid email")

        if len(error) > 0:
            return error
        else:
            hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            self.create(name=name.capitalize(),alias=alias.capitalize(),email=email,password=hash1)
            return error

    def loging(self,form_data):

        email=form_data['email']
        password=form_data['password']
        error=[]

        if len(email) == 0 or len(password) == 0:
            error.append("Invalid Email or Password")
            return error

        user=self.filter(email=email)
        if len(user) == 0:
            error.append("Invalid Email or Password")
            return error

        user1=user[0]
        if not bcrypt.checkpw(password.encode(), user1.password.encode()):
            error.append("Invalid Email or Password")
            return error
        else:
            return user1.id

    def selecting_user(self,user_id):
        # user=self.get(id=user_id)
        # context={
        #     "user":user
        # }
        # return context
        user=self.raw("select * from users_user where id ="+ user_id)
        return user

    def author_creating(self,form_data,user_id):

        error=[]
        author_name=str(form_data['author'])
        book_title=str(form_data['book_title'])
        author_select=form_data['author_select']
        review=str(form_data['review'])
        rating=form_data['rating']

        if len(book_title) < 2:
            error.append("Book Title must be atleast more then 2 characters")
        if author_select == "" and len(author_name) == 0:
            error.append("Choose either given authors or make a new one!!!!")
        if len(review) < 2:
            error.append("Reviws must have atleast 10 characters")
        if rating == "":
            error.append("Enter some Rating for this book!!!")
        if len(error) > 0:
            return error

        if len(author_name)!= 0:
            if str.isalpha(author_name) == False:
                error.append("Author's name shouldn't be empty or any digit")
            if len(author_name)< 2:
                error.append("Author's name invalid!!!")
            if len(error) > 0:
                return error
            else:
                author=Authors.object.create(name=author_name.capitalize())
                author_id=author.id
                book=Book.object.create(title=book_title, user_id=user_id, author_id=author.id)
                return True
        else:
            author = Authors.object.filter(id=author_select)
            if len(author)>0:
                author_id=author[0]
            book=Book.object.create(title=book_title,user_id=user_id,author_id=author_id.id)
            return True


    def selecting_all_authors(self):
        authors=Authors.object.all()
        return authors


class User(models.Model):
    name=models.CharField(max_length=255)
    alias=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=UserManager()


