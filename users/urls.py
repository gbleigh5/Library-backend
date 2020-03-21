from django.conf.urls import include

path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
