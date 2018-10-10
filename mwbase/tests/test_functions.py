from decimal import Decimal

from ..functions import json_dumps


def test_json_dump():
    assert json_dumps({"foo": Decimal("5")}) == '{"foo": "5"}'
