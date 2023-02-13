from django.urls import path

from characters.views import get_random_character_view

urlpatterns = [
    path("character/random/", get_random_character_view, name="character-random"),
]

app_name = "characters"
