from django.db import models
from django.urls import reverse

# Create your models here.
class test(models.Model):
    name=models.CharField(max_length=64)
    cross=models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('detail',kwargs={'pk':self.pk})
