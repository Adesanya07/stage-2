from django.db import models

class Person(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name