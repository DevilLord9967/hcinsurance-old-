from django.db import models
from client.models import Client


class Policy(models.Model):
    plan_number = models.IntegerField()
    name = models.CharField(max_length=100)
    benefits = models.TextField()
    min_sum = models.IntegerField()
    max_sum = models.IntegerField(blank=True)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    min_payterm = models.IntegerField()
    max_payterm = models.IntegerField()

    def __str__(self):
        return self.name

class Client_Policy(models.Model):
    uname=models.EmailField()
    plan_number = models.IntegerField()
    policy_number = models.IntegerField()
    paying_term = models.IntegerField()
    maturity_term = models.IntegerField()
    premium = models.IntegerField()
    mode = models.CharField(max_length=20)
    DOC = models.DateTimeField()

    def __str__(self):
        return self.uname

