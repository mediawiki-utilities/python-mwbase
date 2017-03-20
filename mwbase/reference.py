from . import target, util
from .attr_dict import AttrDict


class Reference(AttrDict):

    def from_json(self, reference_doc):
        return normalize(reference_doc)


def normalize(reference_doc):
    assert False
