from django.urls import path
from api.v1 import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('auth/login', views.TodoListApiView.as_view(), name="auth-login"),
    path('test/params/<str:object_id>', views.TestParams.as_view(), name="test-params"),
    path('user/all', views.ListUser.as_view()),
    #User Registration and User Login
    path('user/register', views.UserRegistration.as_view(), name='register-user'),
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #profile urls
    path('user/profile/list', views.ProfileListView.as_view(), name="profile-listing"),
    path('user/profile/create', views.ProfileCreateView.as_view(), name="profile-create"),
    path('user/profile/<str:object_id>/detail', views.ProfileDetailView.as_view(), name="profile-detail"),
    path('user/profile/<str:object_id>/delete', views.ProfileDeleteView.as_view(), name="profile-detail"),
]