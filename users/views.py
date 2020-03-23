from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
