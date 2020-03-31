from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.CharField(max_length=200)


