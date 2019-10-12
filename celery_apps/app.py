from celery import Celery

app = Celery('celery_apps')

# app.config_from_object("base.celery_config")
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/1'


app.conf.beat_schedule = {
    "run-every-5-seconds": {
        "task": "celery_apps.schedule.tasks.crontab_task",
        "schedule": 5
    },
}