from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            validate_email(email)
        except ValidationError:
            return Response("Invalid email format.", status=status.HTTP_400_BAD_REQUEST)
        
        if len(password) < 8:
            return Response("Password must be at least 8 characters", status=status.HTTP_400_BAD_REQUEST)
    
        return redirect('menu')  # If valid information, then redirect to menu
    return redirect('home')
