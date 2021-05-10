from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


urlpatterns = [
    path('register/', views.BaseUserCreateView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('users/', views.UserListCreateView.as_view(), name='users'),
    path('users/<int:user_id>/', views.UserRetrieveUpdateView.as_view(), name='user-get-update'),
]
