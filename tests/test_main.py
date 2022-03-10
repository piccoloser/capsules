# simple test to make sure everything is working

from app import constants


def test_int():
    assert 1 == 1


def test_imports():
    assert isinstance(constants.APP_VERSION, str)
