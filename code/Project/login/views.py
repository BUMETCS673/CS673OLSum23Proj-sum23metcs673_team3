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

# Create your views here.

#umamaheswar
def user_login(request):
    return render(request, 'login.html', )

#umamaheswar
def user_register(request):
    return render(request, 'registration.html')

@api_view(['POST'])
def auth_user(request):
    print(request)
    password = request.data.get("password")
    username = request.data.get("username")
    user = authenticate(username=username,password=password)
    if user is not None:

        print(user.username)
        data = {
            "user_pass": password,
        }
        response = redirect('/login/homepage/')
    else:
        data = {
            "user_pass": "unauthorized"
        }
        response = Response(data, status=403)

    return response

@api_view(['POST'])
def create_new_user(request):
    password = request.data.get("password")
    username = request.data.get("username")
    email = request.data.get("email")
    user = User.objects.create_user(password=password,username=username,email=email)
    # This token can only be creted once per user need to look into how to expire it
    # token = Token.objects.create(user=user,)
    user.save()
    data = {
        "username":username
    }
    return Response(data,status=200)

def homepage(request):
    return render(request,"homepage.html")