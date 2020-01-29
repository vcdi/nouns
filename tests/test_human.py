from nouns.obj import (
    is_all_integers,
    is_groupable_type,
    is_iterable,
    is_numeric,
    is_numeric_type,
)


def test_ifs():
    s = "a b c"
    assert is_iterable(s.split()) is True

    # nouns considers strings as not iterable
    # even tho they are from a python perspective
    assert is_iterable(s) is False

    assert is_numeric(5) is True
    assert is_numeric_type(float) is True

    assert is_groupable_type(type("group")) is True
    assert is_groupable_type(type(5)) is False

    assert is_all_integers([1, 2, 3.0]) is True
    assert is_all_integers([1, 2, 3.1]) is False
    assert is_all_integers([1, 2, "a"]) is False
