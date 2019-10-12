# from add
import datetime
from unittest.mock import patch

from celery_apps.base import add
from test.utils.celery_mock import mock_delay


def test_producer_base():
    assert add.delay(5, 3).get(5) == 8
    assert add.delay(7, 13).get(5) == 20
    print("finish")


def test_producer_delay():
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


def test_mock_consumer():
    """
    可以直接在本地调试 consumer 代码
    pycharm 如果要直接调试，参数中加入 -k 'test_mock_consumer'
    :return:
    """
    with patch('celery.app.task.Task.delay', mock_delay):
        print(add.delay(5, 34).get(5)==39)
    with patch('celery.app.task.Task.delay', mock_delay):
        # 这个是失效的，因为只是 mock delay 中的方法
        print(add.apply_async(args=(5, 5)).get(5)==10)