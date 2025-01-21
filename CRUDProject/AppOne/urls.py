from django.urls import path
from .views import BookView, BookDetailView

urlpatterns = [
    path('book/', BookView.as_view(), name='books'),
    path('book/<int:pk>/', BookView.as_view(), name="book_with_id")
]
