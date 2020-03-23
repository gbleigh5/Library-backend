from django.conf.urls import include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('token-auth/', obtain_auth_token, name='token_auth'),
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view())
]
