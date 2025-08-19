from django.shortcuts import render
from .models import Restaurant, MenuItem, Contact, RestaurantLocation
from .serializers import MenuItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

def display_home_page_view(request):
    try:
        restaurant = Restaurant.objects.first()
        restaurant_location = RestaurantLocation.objects.first()
        open_close_hours = Contact.objects.first()
        return render(request, "homepage.html", {
            "restaurant_name":restaurant.name, 
            'restaurant_phone_number':restaurant.phone_number,
            'menu_items', MenuItem.objects.all(),
            "restaurant_address": restaurant_location.address,
            "opening_hours":open_close_hours.opening_hours,
            "closing_hours":open_close_hours.closing_hours
        })
    except Restaurant.DoesNotExist:
        return render(request, "homepage.html")

@api_view(['GET'])
def menu_item_view(request):
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def feedback_form_view(request):
    return render(request, "feeback_form.html")

def contact_form_view(request):
    try:
        name = request.GET['name']
        email = request.GET['email']
        validate_email(email)
        
        return Response("We will reach out to you to to fix your problem.", status=status.HTTP_200_OK)
    except KeyError:
        return Response("Invalid credentials.", status=status.HTTP_400_BAD_REQUEST)
    except ValidationError:
        return Response("Email does not exist.", status=status.HTTP_404_NOT_FOUND)

    # If there are no errors store in contact model
    Contact.objects.create({
        'name':name,
        'email':email,
    })

def search_menu_view(request, pk):
    menu_item = get_object_or_404(MenuItem, pk=pk)
    if serializer.is_valid():
        return render(request, "homepage.html", "menu_items":menu_item,)
    return render(request, "homepage.html")