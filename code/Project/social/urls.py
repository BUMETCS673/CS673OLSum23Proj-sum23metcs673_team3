from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index, name='social'),
    path("all_profile/", views.all_profile, name="all_profile"),
    path("profile/<int:pk>", views.profile, name="profile"),
]
