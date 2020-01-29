def tv(thing):
    return thing["_nouns"], thing.get("_v", "MISSING")


def test_prepro_text(x):
    pre = x("hello")
    assert tv(pre) == ("text", "hello")


def test_prepro_number(x):
    pre = x(0)
    assert tv(pre) == ("number", "0")


def test_prepro_it(x):
    pre = x([1, 2])
    assert tv(pre) == ("iterable", "MISSING")


def test_prepro_mapp(x):
    pre = x(dict(a=1, b=2))
    assert tv(pre) == ("mapping", "MISSING")


def test_prepro_obj(x):
    class Something:
        a = 1

    s = Something()
    assert not isinstance(s, str)

    pre = x(s)
    assert tv(pre) == ("mapping", "MISSING")
