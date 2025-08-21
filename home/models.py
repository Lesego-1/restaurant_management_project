from django.db import models
from django.contrib.auth.models import User

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
    opening_hours = models.TimeField(auto_now_add=False)
    closing_hours = models.TimeField(auto_now_add=False)
    phone_number = models.IntegerField()
    logo = models.ImageField()

    def __str__(self):
        return f"Restaurant address: {self.address}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class CartItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class FAQBody(models.Model):
    text = models.CharField(max_length=10000)

    def __str__(self):
        return self.text

class FAQ(models.Model):
    title = models.CharField(max_length=100)
    body = models.OneToOneField(FAQBody, on_delete=models.CASCADE)

    def __str__(self):
        return self.title