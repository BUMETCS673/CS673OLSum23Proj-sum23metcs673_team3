from django.urls import path
from . import views


# URLConf #Umamaheswar
urlpatterns = [

    path('user/', views.user_login, name='User_Login'),
    path('register/', views.user_register, name='register'),
    path('api-auth/',views.auth_user),
    path('register-user/',views.create_new_user),
    path('homepage/',views.homepage),
    path('logout/',views.user_logout, name='User_Logout')

]
