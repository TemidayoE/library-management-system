from rest_framework import serializers
from lib_app.models import Book

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['id','title','author', 'genre','publication_date','is_available','edition','description', ]