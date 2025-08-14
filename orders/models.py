from django.db import models
from home.models import MenuItem
from account.models import UserProfile

class Orders(models.Model):
    customer = models.OneToOneField(UserProfile, on_delete=modelsCASCADE)
    order_items = models.ManyToManyField(MenuItem, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.BooleanField(default=False)  # Set default to False to show order is not done

    def __str__(self):
        return f"{self.customer} ordered: {self.order_items}"