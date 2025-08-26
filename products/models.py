from django.db import models
from django.core.auth.models import User

class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_name)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)