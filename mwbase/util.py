import json


def ensure_decoded_json(val):
    if isinstance(val, dict):
        return val
    else:
        return json.loads(val)
