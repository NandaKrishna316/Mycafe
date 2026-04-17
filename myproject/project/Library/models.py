from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Theme(models.Model):
    genere = models.CharField(max_length=100)
    discription = models.TextField(max_length=1050)

    def __str__(self):
        return self.discription
