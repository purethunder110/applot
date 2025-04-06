import logging
import os
from datetime import datetime

import requests
from django.apps import apps

log = logging.getLogger(__name__)


def get_telegram_bot_instance():
    telegram_bot = apps.get_app_config("core").telegram_bot
    return telegram_bot


class TelegramBot:
    def __init__(self):
        self.telegram_base_url = (
            "https://api.telegram.org/bot7620019512:AAF0Gyi_kpgXxqhRNrIRF8W0O1axW0O5uVw"
        )

    def clean_update_message(self, message_data):
        """
        convery update data from junk to usable data.
        """
        data_chunk = []
        if (
            message_data.get("ok")
            and message_data.get("ok") == True
            and message_data.get("result")
        ):
            for datashard in message_data.get("result"):
                data_chunk.append(
                    {
                        "chat_id": datashard["message"]["chat"]["id"],
                        "first_name": datashard["message"]["from"]["first_name"],
                        "last_name": datashard["message"]["from"]["last_name"],
                        "time": datetime.fromtimestamp(datashard["message"]["date"]),
                        "message": datashard["message"]["text"],
                        # "chat_type":datashard["message"]["entity"][0]["type"]
                    }
                )
            return True, data_chunk
        else:
            return False, data_chunk

    def get_bot_update(self):
        return requests.get(f"{self.telegram_base_url}/getUpdates").json()

    def send_message(self, chat_id: int, message_text: str):
        message_url = f"{self.telegram_base_url}/sendMessage"
        resp = requests.post(
            url=message_url, data={"chat_id": chat_id, "text": message_text}
        )
        return resp.json()

    def set_bot_webhook(self):
        webhook_url = f"{self.telegram_base_url}/setWebhook"
        current_url = os.getenv("WEBSITE_BASE_URL")
        response = requests.post(
            url=webhook_url, data={"url": f"{current_url}/webhook/telegram/"}
        )
        return response.json()
