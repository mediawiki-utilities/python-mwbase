from .attr_dict import AttrDict


class Sitelink(AttrDict):

    @classmethod
    def from_json(cls, datavalue_doc):
        return normalize(datavalue_doc)


def normalize(sitelink_doc):
    return Sitelink({
        'title': sitelink_doc['title'],
        'badges': sitelink_doc.get('badges', [])
    })
