from django.urls import path
from lib_app.views import BookListCreateView, BookRetrievalUpdateDeleteView

urlpatterns = [
    path('v1/books/', BookListCreateView.as_view(), name = 'create-book'),
    path('v1/books/<pk>/', BookRetrievalUpdateDeleteView.as_view(), name = 'book-details'),
]
