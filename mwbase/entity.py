from . import claim, util
from .attr_dict import AttrDict


class Entity(AttrDict):

    @classmethod
    def from_json(cls, entity_doc):
        return normalize(entity_doc)


def normalize(entity_doc):
    entity_doc = util.ensure_decoded_json(entity_doc)
    return Entity({
        'title': entity_doc.get('title'),
        'labels': {
            lang: val['value']
            for lang, val in (entity_doc.get('labels', {}) or {}).items()
            if 'removed' not in val},
        'descriptions': {
            lang: val['value']
            for lang, val in (entity_doc.get('descriptions', {}) or {}).items()},
        'aliases': {
            lang: [a['value'] for a in aliases]
            for lang, aliases in (entity_doc.get('aliases') or {}).items()},
        'claims': {
            pid: [claim.normalize(claim_doc)
                  for claim_doc in claim_docs]
            for pid, claim_docs in (entity_doc.get('claims', {}) or {}).items()},
        'sitelinks': {
            dbname: {'title': val['title'], 'badges': val.get('badges', [])}
            for dbname, val in (entity_doc.get('sitelinks', {}) or {}).items()}
    })
