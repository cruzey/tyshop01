from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100, default='hi')
    image = models.ImageField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)