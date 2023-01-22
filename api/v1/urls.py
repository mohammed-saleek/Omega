from django.urls import path
from api.v1 import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('auth/login', views.TodoListApiView.as_view(), name="auth-login"),
    path('test/params/<str:object_id>', views.test_params.as_view(), name="test-params"),
    path('user/all', views.ListUser.as_view()),
    
    path('user/register', views.UserRegistration.as_view(), name='register-user'),
    
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]