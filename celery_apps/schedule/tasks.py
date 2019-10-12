import logging

from celery_apps.app import app

logger = logging.getLogger("scheduleer")
@app.task
def crontab_task():
    print("crontab_task running")
    logger.info("this is a log message")
