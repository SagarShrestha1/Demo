from django.db import models

# Create your models here.
class post(models.Model):
    name = models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return f"{self.name} and its description (self.description)"

