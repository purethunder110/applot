from django.urls import path

from .views import *

urlpatterns = [
    path("test_Anime/", test_view, name="test_anime"),
    path("", Spotlight.as_view(), name="landing page"),
    path("search/<str:search_term>", searchPage.as_view(), name="anime search page"),
    path("episode", episode_page.as_view(), name="episode_page"),
]
