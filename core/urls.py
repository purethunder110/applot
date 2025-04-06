from django.urls import path

from .views import *

urlpatterns = [
    path("", Spotlight.as_view(), name="Landing page"),
    path("webhook/<str:webhook_type>/", WebhookView.as_view(), name="telegram page"),
]
