from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# from login.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
# from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse #trail #mahesh
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # check if user is authenticated
        user = authenticate(username=username, password=password)
        if user is not None: # if there's such user, redirect to homepage
            login(request, user)
            response = redirect('/login/homepage/')
        else: # otherwise, go back to login page
            response = redirect('/login/user/')
        return response
    return render(request, 'login.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        raw_password = request.POST['password']
        user = User.objects.create_user(username, email, raw_password)
        user.save()
        return redirect('/login/user/')
    return render(request, 'registration.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/homepage/')
    return render(request, 'logout.html')


@api_view(['POST'])
def auth_user(request):
    print(request)
    password = request.data.get("password")
    username = request.data.get("username")
    user = authenticate(username=username,password=password)
    if user is not None:
        #This token can only be creted once per user need to look into how to expire it
        # token = Token.objects.create(user=user,)
        print(user.username)
        data = {
            "user_pass": password,
            # "token": token.key
        }
        response = redirect('/login/homepage/')
    else:
        data = {
            "user_pass": "unauthorized"
        }
        response = Response(data, status=403)

    # print(user[0])
    return response

@api_view(['POST'])
def create_new_user(request):
    password = request.data.get("password")
    username = request.data.get("username")
    email = request.data.get("email")
    user = User.objects.create_user(password=password,username=username,email=email)
    user.save()
    data = {
        "username":username
    }
    return Response(data,status=200)

def homepage(request):
    return render(request,"homepage.html")