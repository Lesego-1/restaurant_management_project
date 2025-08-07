from django.shortcuts import render
from .models import Restaurant, MenuItem

def display_home_page_name(request):
    items = MenuItem.objects.all()  # Get all menu items
    return render(request, "homepage.html", {"restaurant_name":Restaurant.objects.first().name, "menu_items":items})