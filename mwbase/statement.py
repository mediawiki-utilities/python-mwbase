from decimal import Decimal

from . import datavalue
from .attr_dict import AttrDict


class Statement(AttrDict):

    def from_json(self, datavalue_doc):
        return normalize(datavalue_doc)


def normalize(statement_doc):
    return Statement({
        'property': statement_doc['property'],
        'snaktype': statement_doc['snaktype'],
        'datatype': statement_doc['datatype'],
        'datavalue': datavalue.normalize(statement_doc['datavalue'])
    })
