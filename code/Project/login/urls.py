from django.urls import path
from . import views
from django.urls import path
#from .views import google_login, google_auth_callback

# URLConf
urlpatterns = [

    path('', views.user_login, name='login'),
    path('manage/', views.manage, name='manage'),
    path('register/', views.user_register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('reset/<uidb64>/<token>', views.reset_pass_done, name='reset_pass_done'),
    #path('google/', views.google_login, name='google_login'),  #Use these paths only if you implement custom google Auth Function
    #path('google-auth-callback/', views.google_auth_callback, name='google_auth_callback'),  #Use these paths only if you implement custom google Auth Function

]
