from django.urls import path

from .views import *

urlpatterns = [
    path("", Spotlight.as_view(), name="Landing page"),
    path("health_checkup",healthCheckup.as_view(),name="health checkup"),
    path("webhook/<str:webhook_type>/", WebhookView.as_view(), name="webhooks"),
]
