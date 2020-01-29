from pytest import fixture

from nouns import get_x


@fixture
def x():
    _x = get_x()
    yield _x
