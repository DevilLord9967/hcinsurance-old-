from django.db import models
from datetime import datetime


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    DOB = models.DateTimeField()
    mobile1 = models.CharField(max_length=20)
    mobile2 = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Reciept(models.Model):
    client_name = models.ForeignKey(Client, on_delete=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='Premium_Reciept/%Y-%m-%d/')

    def __str__(self):
        return self.client_name.name


