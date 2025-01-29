from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  genre = models.CharField(max_length=255)
  publication_date = models.DateField(("15-01-2004"), auto_now=True, auto_now_add=False, null = True)
  is_available = models.BooleanField(default=True)
  edition = models.CharField(max_length=255)
  description = models.TextField(null= True,blank=True)
  
  def __str__(self):
      return self.title
  