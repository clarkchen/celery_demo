from celery import Celery

app = Celery('celery_apps')

# app.config_from_object("base.celery_config")
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/1'
