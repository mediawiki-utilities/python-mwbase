import json

DATATYPE_MAP = {
    'wikibase-entityid': 'wikibase-item',
    'globecoordinate': 'globe-coordinate'
}


def normalize_datatype(datatype):
    return DATATYPE_MAP.get(datatype, datatype)


def ensure_decoded_json(val):
    if isinstance(val, dict):
        return val
    else:
        return json.loads(val)
