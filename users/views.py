from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework import status
from .models import User
from .serializers import UserSerializer, UserBorrowedBooksSerializer
import json

class UserList(APIView):
    def get(self, request, format=None):
        permission_classes = [IsAuthenticated, IsAdminUser]
        User = get_user_model()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return add_user_type(request)

@api_view(["POST"])
@csrf_exempt
def add_superuser(request):
    return add_user_type(request, 'SUPERUSER')

def add_user_type(request, type='USER'):
    try:
        User = get_user_model()
        payload = json.loads(request.body)
        if payload["password"] != payload["password2"]:
            return JsonResponse({'error': "Passwords don't match"}, status=status.HTTP_400_BAD_REQUEST)

        del payload["password2"] # remove password2 because not needed in model
        serializer = UserSerializer(data=payload)
        if not serializer.is_valid():
            return JsonResponse({'error': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST)

        if type == 'SUPERUSER':
            User.objects.create_superuser(**payload)
        else:
            User.objects.create_user(**payload)
        return JsonResponse({}, safe=False, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'Something terrible went wrong'},
            safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserBorrowedBooks(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserBorrowedBooksSerializer
