import logging

logger = logging.getLogger(__name__)


def run_birthday_greetings():
    from .tasks import send_birthday_greetings_task
    try:
        send_birthday_greetings_task()
    except Exception as e:
        logger.error("run_birthday_greetings xatolik: %s", e)