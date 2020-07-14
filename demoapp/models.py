from django.db import models



class Author (models.Model):
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    name = models.CharField(max_length=150)
    published_year = models.IntegerField()
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

