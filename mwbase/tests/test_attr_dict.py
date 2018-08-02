from collections import OrderedDict

from ..attr_dict import AttrDict


def test_attr_dict():
    d1 = AttrDict([("foo", AttrDict([("bar", 1)]))])
    d2 = AttrDict([("foo", AttrDict([("bar", 1)]))])

    assert d1 == d2


def test_ordered_dict():
    d1 = OrderedDict([("foo", OrderedDict([("bar", 1)]))])
    d2 = OrderedDict([("foo", OrderedDict([("bar", 1)]))])

    assert d1 == d2
