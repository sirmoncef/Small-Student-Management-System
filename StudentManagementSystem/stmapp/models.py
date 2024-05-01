from django.db import models

class Student(models.Model):
    Departement_choices = [
        ('Preparatory Cycle','CP'),
        ('Super Cycle','CS'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    phonenumber = models.CharField(max_length=100)
    Departement = models.CharField(max_length=50,choices=Departement_choices)


    def __str__(self):
        return self.name


