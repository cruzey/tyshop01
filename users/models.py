from django.db import models
from django.contrib.auth.models import AbstractUser
from tyadmins.models import Product

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=40)
    phonenum = models.CharField(max_length=20, null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField()
    order_id = models.CharField(max_length=40, null=True)
