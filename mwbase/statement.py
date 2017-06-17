from . import claim, util
from .attr_dict import AttrDict


class Statement(AttrDict):

    @classmethod
    def from_json(cls, statement_doc):
        return normalize(statement_doc)


def normalize(statement_doc):
    statement_doc = util.ensure_decoded_json(statement_doc)

    references = {}
    for item in statement_doc.get('references', []):
        for pid, ref_docs in item['snaks'].items():
            references[pid] = [claim.normalize(ref_doc)
                               for ref_doc in ref_docs]

    return Statement({
        'id': statement_doc.get('id'),
        'hash': statement_doc.get('hash'),
        'claim': claim.normalize(statement_doc['mainsnak']),
        'rank': statement_doc.get('rank', None),
        'references': references,
        'qualifiers': {
            prop: [claim.normalize(qualifier_doc)
                   for qualifier_doc in statement_doc['qualifiers'][prop]]
            for prop in statement_doc.get('qualifiers-order', [])}
    })
