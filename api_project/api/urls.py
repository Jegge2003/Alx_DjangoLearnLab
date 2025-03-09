# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Optional: existing ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),

    # ViewSet URLs managed by the router
    path('', include(router.urls)),
]
