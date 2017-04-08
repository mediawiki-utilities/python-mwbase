from . import datavalue
from .attr_dict import AttrDict


class Statement(AttrDict):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize(datavalue_doc)


def normalize(statement_doc):
    return Statement({
        'property': statement_doc['property'],
        'snaktype': statement_doc['snaktype'],
        'datavalue': datavalue.normalize(statement_doc['datavalue']),
        'datatype': statement_doc.get('datatype'),
        'hash': statement_doc.get('hash')
    })
