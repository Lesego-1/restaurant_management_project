from django.shortcuts import render
from .models import Restaurant

def display_home_page_name(request):
    return render(request, "homepage.html", {"restaurant_name":Restaurant.objects.first().name})