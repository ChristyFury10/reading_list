from django.db import models

# Create your models here.
class Author(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    
    def __str__(self):
        return self.title
    
class BookList(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
