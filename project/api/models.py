from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=40)
    shop_established = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name