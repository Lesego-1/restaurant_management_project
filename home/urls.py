from django.urls import path
from .views import *

urlpatterns = [
    path("home/", display_home_page_view, name="homepage"),
    path("feedback/", fee)
]