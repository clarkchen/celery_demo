# celery_demo

## start sh
worker start 
cd project root dir

```
celery -A consumer worker --loglevel=info
```

producer start
cd project root dir

```
# python cli
from celery_apps import add
add.delay(5,3)
```