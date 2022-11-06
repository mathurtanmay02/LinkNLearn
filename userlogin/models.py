from django.db import models
# Create your models here.

class authorization(models.Model):
    name = models.CharField(max_length=200, default='' , unique=True)
    position = models.CharField(max_length= 50, default='', null = False)
    company_name = models.CharField(max_length=50, default='', null = False)
    email = models.EmailField()

    def __str__(self):
        return self.name