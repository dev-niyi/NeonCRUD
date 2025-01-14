from django.urls import path
from .views import AuthorView, AuthorDetailView

urlpatterns = [
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]
