from django.urls import path
from api.v1 import views

urlpatterns = [
    path('auth/login', views.TodoListApiView.as_view(), name="auth-login"),
]