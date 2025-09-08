from django.urls import path
from .views import *

urlpatterns = [
    path("home/", display_home_page_view, name="homepage"),
    path("feedback/", feedback_form_view, name="feedback_form"),
    path("menu_item/", menu_item_view, name="menu_item_view"),
    path("privacy_policy/", privacy_policy_view, name="privacy_policy"),
    path("thank_you/", thank_you_page_view, name="thank_you"),
    path("our_story/", our_story_view, name="our_story"),
    path("reservations/", reservations_view, name="reservations"),
    path("our_team/", our_team_view, name="our_team"),
]