import pytest


@pytest.fixture()
def setUp():
    print("------开始计算------")
    yield
    print("------计算结束------")
