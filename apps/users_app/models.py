from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta
import re

EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
noNumberPls = re.compile(r'^[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = []

        if 'email' in postData:
            if len(postData['email']) == 0:
                errors.append('Please enter your email address!')
            elif not EMAIL_REGEX.match(postData['email']):
                errors.append('Please enter a valid email address!')

        if 'first_name' in postData:
            if len(postData['first_name']) == 0:
                errors.append('Please enter your first name!')
            elif len(postData['first_name']) < 2:
                errors.append('First name should be no fewer than 2 letters')
            elif not noNumberPls.match(postData['first_name']):
                errors.append('First name should have no numbers or special characters in it!')

        if 'last_name' in postData:
            if len(postData['last_name']) == 0:
                errors.append('Please enter your last name!')
            elif len(postData['last_name']) < 2:
                errors.append('Last name should be no fewer than 2 letters!')
            elif not noNumberPls.match(postData['last_name']):
                errors.append('Last name should have no numbers or special characters in it!')

        if 'password' in postData:
            if len(postData['password']) == 0:
                errors.append('Please enter your password!')
            elif len(postData['password']) < 8:
                errors.append('Password should be no fewer than 8 characters!')
            elif postData['password'] != postData['conf_pass']:
                errors.append('Password Confirmation do not match our record!')

        if 'birthday' in postData:
            if len(postData['birthday']) == 0:
                errors.append('Please enter your birth date')
            else:
                birthday = postData['birthday']
                date_format = "%Y-%m-%d"
                birth = datetime.strptime(birthday, date_format).date()
                now = datetime.now().date()

                if birth > now:
                    errors.append('Birthdate must be in the past!')
                elif birth == now:
                    errors.append('Please enter correct birthday!')
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()