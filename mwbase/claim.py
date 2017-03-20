from . import statement, util
from .attr_dict import AttrDict


class Claim(AttrDict):

    @classmethod
    def from_json(cls, claim_doc):
        return normalize(claim_doc)


def normalize(claim_doc):
    claim_doc = util.ensure_decoded_json(claim_doc)

    references = {}
    for item in claim_doc.get('references', []):
        for pid, ref_docs in item['snaks'].items():
            references[pid] = [statement.normalize(ref_doc)
                               for ref_doc in ref_docs]

    return Claim({
        'id': claim_doc.get('id'),
        'hash': claim_doc.get('hash'),
        'statement': statement.normalize(claim_doc['mainsnak']),
        'rank': claim_doc.get('rank', None),
        'references': references,
        'qualifiers': {
            prop: [statement.normalize(qualifier_doc)
                   for qualifier_doc in claim_doc['qualifiers'][prop]]
            for prop in claim_doc.get('qualifiers-order', [])}
    })
