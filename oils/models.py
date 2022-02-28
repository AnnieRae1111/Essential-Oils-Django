from django.db import models

# Create your models here.

class EssentialOils(models.Model):
    name=models.CharField(max_length =100)
    benefits=models.CharField(max_length=1000)
    aromatic_description= models.CharField(max_length=1000)
    photo_url=models.TextField()

    def __str__(self):
        return self.name