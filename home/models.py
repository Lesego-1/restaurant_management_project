from django.db import models

class MenuItem(models.Model):
    restaurant = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_available = models.BooleanField(default=True)  # Set default availability to True
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: ${self.price}"