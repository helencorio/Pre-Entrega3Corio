from django.db import models

# Create your models here.


class Student():
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    mail = models.EmailField()

class Tutor(models.Model, Student):
    pass