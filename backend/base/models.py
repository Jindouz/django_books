from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
   
    def __str__(self):
        return f'{self.name} {self.author} {self.year}'
