import logging

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .utils import get_telegram_bot_instance

# Create your views here.

log = logging.getLogger(__name__)


class Spotlight(View):
    def __init__(self):
        self.list_of_url = ["anime", "admin", "config", "telegram"]

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            response = self.loading_page(request)
        elif request.method == "OPTIONS":
            self.http_method_names = ["get", "options"]
            response = self.options()
        return response

    def loading_page(self, request):
        return render(
            request, "html/spotlight_landing.html", {"list_of_urls": self.list_of_url}
        )


class healthCheckup(View):
    def __init__(self):
        self.health_checkup_channel_id = "-4754204346"

    def dispatch(self, request):
        self.health_checkup(request)
        return HttpResponse(status=200)

    def health_checkup(self, request):
        telegram_bot = get_telegram_bot_instance()
        telegram_bot.send_message(
            self.health_checkup_channel_id, "The state of applot is healthy"
        )


class WebhookView(View):
    def __init__(self):
        self.telegram_base_url = (
            "https://api.telegram.org/bot7620019512:AAF0Gyi_kpgXxqhRNrIRF8W0O1axW0O5uVw"
        )

    def dispatch(self, request, webhook_type=None):
        if webhook_type == "telegram":
            response = self.telegram_webhook(request)
        else:
            log.warning(
                f"WEBHOOK VIEW not set webhook hitting the server | webhook_type:{webhook_type}"
            )
            return HttpResponse(status=404)
        return JsonResponse(response)

    def telegram_webhook(self, request):
        log.info(f"webhook data | {request}")
        telegram_bot = get_telegram_bot_instance()
        get_updates = telegram_bot.get_bot_update()
        valid, cleared_message = telegram_bot.clean_update_message(get_updates)
        if valid:
            resp = telegram_bot.send_message(
                cleared_message[-1]["chat_id"],
                f"hi, this is a test message, you ran {cleared_message[-1]['message']}",
            )
            log.info(f"webhook send mesage | respones:{resp}")
        return {}
