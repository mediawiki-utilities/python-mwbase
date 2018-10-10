import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
     def default(self, obj):
         if isinstance(obj, Decimal):
             return str(obj)
         # Let the base class default method raise the TypeError
         return json.JSONEncoder.default(self, obj)


def json_dumps(*args, **kwargs):
    return json.dumps(*args, cls=DecimalEncoder, **kwargs)

def json_dump(*args, **kwargs):
    return json.dump(*args, cls=DecimalEncoder, **kwargs)
