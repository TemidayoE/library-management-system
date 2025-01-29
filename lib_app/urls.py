from django.urls import path
from lib_app.views import BookListCreateView, BookRetrievalUpdateDeleteView

urlpatterns = [
    path('', lambda request: HttpResponse('Welcome to the Library Management System API!')),
    path('v1/books/', BookListCreateView.as_view(), name = 'create-book'),
    path('v1/books/<pk>/', BookRetrievalUpdateDeleteView.as_view(), name = 'book-details'),
]
