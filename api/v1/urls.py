from django.urls import path
from api.v1 import views

urlpatterns = [
    path('auth/login', views.TodoListApiView.as_view(), name="auth-login"),
    path('test/params/<str:object_id>', views.test_params.as_view(), name="test-params"),
    path('user/register', views.UserRegistration.as_view()),
    path('user/all', views.ListUser.as_view()),
]