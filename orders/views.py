from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import MenuItem, Order
from .serializer import MenuItemSerializer

@api_view(["GET"])
def get_menu(request):
    queryset = MenuItem
    serializer = MenuItemSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def order_confirmation_view(request, pk):
    order = Order.objects.filter(pk=pk)
    if order.