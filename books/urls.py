from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_books),
    path('', views.add_book),
    path('book/<int:book_id>', views.get_book),
    path('book/<int:book_id>', views.update_book),
    path('book/<int:book_id>', views.delete_book)
]
