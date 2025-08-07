from django.shortcuts import render
from .models import Restaurant, MenuItem
from .serializers import MenuItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def display_home_page_name(request):
    restaurant_name = Restaurant.objects.first()
    if restaurant_name:
        return render(request, "homepage.html", {"restaurant_name":Restaurant.objects.first().name})
    return render(request, "homepage.html")

@api_view['GET']
def menu_item_view(request):
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)