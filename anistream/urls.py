from django.urls import path

from .views import *

urlpatterns = [
    path("test_Anime/", test_view, name="test_anime"),
    path("", Spotlight.as_view(), name="landing page"),
]
