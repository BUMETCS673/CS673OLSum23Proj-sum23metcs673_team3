from django.urls import path
from . import views


# URLConf
urlpatterns = [

    path('', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('reset/<uidb64>/<token>', views.reset_pass_done, name='reset_pass_done')

]
