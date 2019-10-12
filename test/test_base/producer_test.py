# from add
from celery_apps import add
def test_producer_base():
    assert add.delay(5,3).get(5) == 8
    assert add.delay(7,13).get(5)==20
    print("finish")
