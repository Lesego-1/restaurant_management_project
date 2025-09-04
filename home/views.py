from django.shortcuts import render, redirect
from .models import Restaurant, MenuItem, Contact, RestaurantLocation, CartItem, FAQ, AboutTheChef, NewsLetter
from .serializers import MenuItemSerializer, FAQSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from products.models import Special
from django.core.paginator import Paginator
import time

def display_home_page_view(request):
    try:
        restaurant = Restaurant.objects.first()
        restaurant_location = RestaurantLocation.objects.first()
        open_close_hours = Contact.objects.first()
        phone_number = RestaurantLocation.objects.first().phone_number
        logo = RestaurantLocation.objects.first().logo
        cart_items = get_object_or_404(CartItem, owner=request.user)
        chef = AboutTheChef.objects.first()
        menu = MenuItem.objects.all().order_by("-created_by")
        paginator = Paginator(menu, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "homepage.html", {
            "restaurant_name":restaurant.name, 
            'restaurant_phone_number':restaurant.phone_number,
            'menu_items', MenuItem.objects.all(),
            "restaurant_address": restaurant_location.address,
            "opening_hours":open_close_hours.opening_hours,
            "closing_hours":open_close_hours.closing_hours,
            "phone_number":phone_number,
            "logo":logo,
            "cart_items":cart_items,
            "current_time":open_close_hours.time,
            "specials":Special.objects.all(),
            "chef_name":chef.name,
            "chef_bio":chef.bio,
            "page_obj":page_obj,
            "year": time.year(),
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
    name = request.GET['name']
    email = request.GET['email']
    message = request.GET['msg']
    try:
        validate_email(email)
    except KeyError:
        return Response("Invalid Credentials", status=status.HTTP_400_BAD_REQUEST)
    except ValidationError:
        return Response("Email does not exist." status=status.HTTP_404_NOT_FOUND)
    
    Contact.objects.create(
        "name":name,
        "email":email,
        "message":message
    )
    return redirect('thank_you')

def search_menu_view(request, pk):
    menu_item = get_object_or_404(MenuItem, pk=pk)
    serializer = MenuItemSerializer(menu_item)
    if serializer.is_valid():
        return render(request, "homepage.html", "menu_items":menu_item,)
    return render(request, "homepage.html")

def faq_view(request):
    faq = FAQ.objects.all()
    serializer = FAQSerializer(faq, many=True)
    if serializer.is_valid():
        return render(request, "faq.html", {"faq_objects":faq})
    return render(request, "faq.html")

def privacy_policy_view(request):
    return render(request, "privacy_policy.html")

def thank_you_page_view(request):
    return render(request, "thank_you.html", {'email':request.user.email})

def about_us_view(request):
    return render(request, 'about_us.html', {'description':open_close_hours.about_us})

def news_letter_view(request):
    NewsLetter.objects.create(email=request.POST['email'])

def our_story_view(request):
    return render(request, "our_story.html")

def menu_search(request):
    search_item = request.data['menu_search']
    queryset = MenuItem.objects.filter(name=search_item)
    return render(request, 'menu.html', {'menu_items':queryset})