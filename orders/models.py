from django.db import models
from home.models import UserProfile

class Orders(models.Orders):
    # Customer, order_items, total_amnt, order_status
