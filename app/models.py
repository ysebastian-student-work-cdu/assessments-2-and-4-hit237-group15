from django.db import models

# Create your models here.
class User(models.Model):
    userid  = models.CharField(max_length=200)
    name = models.TextField()
    email = models.TextField()
    role = models.TextField()

    def __str__(self):
        return self.name

