from . import target, util
from .attr_dict import AttrDict


class Reference(AttrDict):

    @classmethod
    def from_json(cls, reference_doc):
        return normalize(reference_doc)


def normalize(reference_doc):
    assert False
