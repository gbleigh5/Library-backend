from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import json

@api_view(["POST"])
@csrf_exempt
def add_user(request):
    try:
        payload = json.loads(request.body)
        if payload["password"] != payload["password2"]:
            return JsonResponse({'error': 'E-mail is already in use'}, status=status.HTTP_400_BAD_REQUEST)
        User = get_user_model()
        user = User.objects.create(
            email=payload["email"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            password=payload["password"],
            phone=payload["phone"]
        )
        serializer = UserSerializer(user)
        return JsonResponse({}, safe=False, status=status.HTTP_201_CREATED)
    except IntegrityError:
        return JsonResponse({'error': 'E-mail is already in use'},
            safe=False, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'},
            safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
