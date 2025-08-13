from django.urls import path
from .views import *

urlpatterns = [
    path("home/", display_home_page_view, name="homepage"),
    path("feedback/", feedback_form_view, name="feedback_form"),
    path("menu_item/", menu_item_view, name="menu_item_view"),
]