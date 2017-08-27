from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
import datetime
from time import gmtime, strftime
import re
import bcrypt
import math
from models import User




# Create your views here.

def index(request):
	print "index"
    return render(request, 'userDashboard/index.html')

# def dashboard(request):
#     #user must be logged in and must be an admin to see page
#     if request.session.get('user_id', False):
#         user = User.objects.get(id=request.session['user_id'])
#         if user.user_level == 9:
#             context = {
#                'users': User.objects.all()
#             }
#             return render(request, 'userDashboard/dashboard.html', context)
#         else:
#             return redirect('/')
#     else:
#         return redirect('/')

# def signin(request):
#     if 'user_id' in request.session:
#         if request.session['isAdmin'] == True:
#             return redirect('/dashboard')
#         return redirect('/products')
#     return render(request, 'userDashboard/login.html')

# def register(request):
#     return render(request, 'userDashboard/registration.html')

# def create_user(request):

# def admin_create_user(request):

# def user(request, user_id):

# def add_user(request):

# def edit_user(request):

# def edit_user_admin(request, user_id):

# def update_user(request, user_id):

# def delete_user(request, user_id):

# def profile(request, user_id):

# def login(request):

# def logout(request):

# def update_password(request, user_id):

# def prodDashboard(request):

# def prodDashboardsearch(request, searchname, page):