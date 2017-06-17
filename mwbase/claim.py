from . import datavalue
from .attr_dict import AttrDict


class Claim(AttrDict):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize(datavalue_doc)


def normalize(claim_doc):
    return Claim({
        'property': claim_doc['property'],
        'snaktype': claim_doc['snaktype'],
        'datavalue': datavalue.normalize(claim_doc.get('datavalue')),
        'datatype': claim_doc.get('datatype'),
        'hash': claim_doc.get('hash')
    })
