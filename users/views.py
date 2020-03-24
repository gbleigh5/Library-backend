from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework import status
from users.models import BorrowedBook
from users.serializers import UserSerializer, BorrowedBooksSerializer
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

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_books(request, user_id):
    borrowed_books = BorrowedBook.objects.filter(user=user_id)
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return JsonResponse({'borrowed_books': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_book(request, user_id, book_id):
    book = BorrowedBook.objects.get(id=book_id, user=user_id)
    serializer = BorrowedBooksSerializer(book)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_books(request, user_id, book_id):
    payload = json.loads(request.body)
    try:
        for book in payload['books']:
            serializer = BorrowedBooksSerializer(data=book)
            if not serializer.is_valid():
                return JsonResponse({'error': serializer.errors, 'book': book.id},
                    status=status.HTTP_400_BAD_REQUEST)

        BorrowedBook.objects.bulk_create(payload['books'])
        return JsonResponse({}, safe=False, status=status.HTTP_201_CREATED)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_book(request, user_id, book_id):
    payload = json.loads(request.body)
    try:
        book_item = BorrowedBook.objects.get(user=user_id, id=book_id)
        book_item.update(**payload)
        book = BorrowedBook.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
