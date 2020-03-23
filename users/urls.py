from django.conf.urls import include
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import status
from . import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.add_user),
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view())
]
