from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.name
