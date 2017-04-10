from decimal import Decimal

from . import util
from .attr_dict import AttrDict


class DataValue(AttrDict):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize(datavalue_doc)


def normalize(datavalue_doc):
    if datavalue_doc is None:
        return None

    datavalue_doc = util.ensure_decoded_json(datavalue_doc)

    if datavalue_doc['type'] == 'wikibase-entityid':
        return normalize_entityid(datavalue_doc)
    elif datavalue_doc['type'] == 'globecoordinate':
        return normalize_coordinate(datavalue_doc)
    elif datavalue_doc['type'] == 'time':
        return normalize_time(datavalue_doc)
    elif datavalue_doc['type'] == 'quantity':
        return normalize_quantity(datavalue_doc)
    elif datavalue_doc['type'] == 'string':
        return normalize_string(datavalue_doc)


class Time(DataValue):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize_time(datavalue_doc)


class EntityId(DataValue):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize_entityid(datavalue_doc)


class Coordinate(DataValue):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize_coordinate(datavalue_doc)


class Quantity(DataValue):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize_quantity(datavalue_doc)


class String(DataValue):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize_string(datavalue_doc)


def normalize_time(datavalue_doc):
    return Time({
        'type': datavalue_doc['type'],
        'timestamp': datavalue_doc['value']['time'],
        'precision': datavalue_doc['value'].get('precision', None),
        'before': datavalue_doc['value']['before'],
        'after': datavalue_doc['value']['after'],
        'timezone': datavalue_doc['value']['timezone'],
        'calendarmodel': datavalue_doc['value']['calendarmodel']
    })


def normalize_entityid(datavalue_doc):
    if 'id' in datavalue_doc['value']:
        id_val = datavalue_doc['value']['id']
    elif datavalue_doc['value']['entity-type'] == 'item':
        id_val = "Q" + str(datavalue_doc['value']['numeric-id'])
    elif datavalue_doc['value']['entity-type'] == 'property':
        id_val = "P" + str(datavalue_doc['value']['numeric-id'])
    else:
        id_val = None
    return EntityId({
        'type': datavalue_doc['type'],
        'entity-type': datavalue_doc['value']['entity-type'],
        'numeric-id': datavalue_doc['value']['numeric-id'],
        'id': id_val
    })


def normalize_coordinate(datavalue_doc):
    return Coordinate({
        'type': datavalue_doc['type'],
        'latitude': datavalue_doc['value']['latitude'],
        'longitude': datavalue_doc['value']['longitude'],
        'altitude': datavalue_doc['value']['altitude'],
        'precision': datavalue_doc['value']['precision'],
        'globe': datavalue_doc['value']['globe']
    })


def normalize_quantity(datavalue_doc):
    if 'upperBound' in datavalue_doc['value']:
        error = {
            'upper': Decimal(str(datavalue_doc['value']['upperBound'])),
            'lower': Decimal(str(datavalue_doc['value']['lowerBound']))
        }
    else:
        error = None

    return Quantity({
        'type': datavalue_doc['type'],
        'value': Decimal(str(datavalue_doc['value']['amount'])),
        'unit': datavalue_doc['value']['unit'],
        'error': error
    })


def normalize_string(datavalue_doc):
    return String({
        'type': datavalue_doc['type'],
        'value': str(datavalue_doc['value'])
    })
