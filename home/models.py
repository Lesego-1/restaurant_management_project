from django.db import models

class MenuItem(models.Model):
    restaurant = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField()
    is_available = models.BooleanField(default=True)  # Set default availability to True
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: ${self.price}"

class RestaurantLocation(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()

    def __str__(self):
        return f"Restaurant address: {self.address}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name