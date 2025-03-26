from django.urls import path
from .views import *

urlpatterns = [
    path("",Spotlight.as_view(),name="Landing page"),
]