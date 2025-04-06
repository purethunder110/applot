import logging
import os

from django.apps import AppConfig

from .utils import TelegramBot

log = logging.getLogger(__name__)


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    telegram_bot = None

    def ready(self):
        # prevent twice run
        run_once = os.environ.get("CMDLINERUNNER_RUN_ONCE")
        if run_once is not None:
            return
        os.environ["CMDLINERUNNER_RUN_ONCE"] = "True"

        # set telegram webhook
        self.telegram_bot = TelegramBot()
