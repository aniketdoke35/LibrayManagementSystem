from django.db import models

# Create your models here.
class Books(models.Model):
    bid = models.IntegerField(primary_key=True)
    bookName = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    publishedYear = models.DateField()


    def __str__(self):
        return self.bookName

