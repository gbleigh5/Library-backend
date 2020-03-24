from django.conf.urls import include
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import status
from . import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('admin/', views.add_superuser),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('<int:pk>/books/', views.get_books),
    path('<int:pk>/books/', views.add_books),
    path('<int:user_id>/book/<int:book_id>/', views.get_book)
]
