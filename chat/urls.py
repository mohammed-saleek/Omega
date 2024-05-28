from django.urls import path
from . import views

urlpatterns = [
    path('user/chat', views.lobby, name="user-chat"),
]