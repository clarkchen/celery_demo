import datetime
from unittest import TestCase

from celery_apps import app
from celery_apps.base.tasks import add

class TestAdd(TestCase):
    def setUp(self) -> None:
        app.conf.task_always_eager = True

    def test_add(self):
        """
        eager model 不需要启动本地代码
        :return:
        """
        assert add.delay(5, 3).get(5) == 8
        assert add.delay(7, 13).get(5) == 20
        assert add.apply_async((133, 2),).get(5) == 135

        print("finish")

    def test_count_donw(self):
        """
        1. 需要禁用 eager
        2. 在根目录执行， celery -A consumer worker --loglevel=info

        :return:
        """
        app.conf.task_always_eager = False

        start = datetime.datetime.now()
        res = add.apply_async(args=(5, 8), countdown=3)
        assert res.get(5) == 13
        end = datetime.datetime.now()
        assert (end - start).total_seconds() > 3
        print("delay test")

        res = add.apply_async(kwargs={"x": 20, "y": 30}, countdown=3)
        assert res.get(5) == 50
        end = datetime.datetime.now()
        assert (end - start).total_seconds() > 3
        print("delay test by kwargs")