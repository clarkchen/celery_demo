from celery_apps.app import app

@app.task
def add(x, y):
    return x + y
