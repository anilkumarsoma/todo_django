from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from managTask.models import Users
import string
import random
from datetime import datetime

# from django.template import loader
# Create your views here.

def index(request):
    # request.session['username'] = 'Sowmya'
    us = ''
    try:
        users = Users.objects.all()
        for user in users:
            if user.email == request.session['email']:
                us = user
                break
        if 'username' in request.session:
            x = request.session['username']
        else:
            x = ''
    except:
        return render(request, 'todo/index.html')
    return render(request, 'todo/index.html',{'user': us,'session_set':request.session['username']})

def login(request):
    # request.session['username'] = 'Sowmya'
    return render(request, 'todo/login.html', {})

def signup(request):
    return render(request, 'todo/signup.html', {})

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def signUpUser(request):
    us = Users(userid=id_generator(), password=request.POST["password"], email=request.POST["email"], phone=request.POST["phone"], username=request.POST["username"])
    us.save()
    return render(request,'todo/index.html')

def loginUser(request):
    user = get_object_or_404(Users, email=request.POST['email'], password=request.POST['password'])
    request.session['username'] = user.username
    request.session['email'] = request.POST['email']
    request.session['id'] = user.id
    return render(request, 'todo/index.html', {'user': user,'session_set':request.session['username']})

