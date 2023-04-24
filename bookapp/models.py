from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    
class Book(models.Model):
    name = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=13)
    sinopsys = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    
class Publishes(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)