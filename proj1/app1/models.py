from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    efnm = models.CharField(max_length=20)
    elnm = models.CharField(max_length=20)
    edob = models.DateField()
    email = models.EmailField()
    eaddr = models.TextField()
    epn = models.BigIntegerField()
