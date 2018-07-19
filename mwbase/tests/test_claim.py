from . import util
from .. import entity


def test_normalize():
    wb_doc = util.load_blob('Q7251')
    Q7251 = entity.normalize(wb_doc)

    assert(Q7251.properties['P268'][0].claim.datavalue['value'] ==
           "12205670t")

    assert({pid for pid, statements in Q7251.properties.items()
            if len(statements) > 1} ==
           {'P1343', 'P800', 'P512', 'P101', 'P108', 'P69', 'P106', 'P19',
            'P166'})

    assert(Q7251.properties['P21'][0].claim.datavalue['id'] ==
           "Q6581097")

    assert({(pid, ref_claims[0]['datavalue']['type'])
            for pid, ref_claims in Q7251.properties['P21'][0].references.items()} ==
           {('P143', 'wikibase-entityid'),
            ('P813', 'time'),
            ('P248', 'wikibase-entityid')})

    wb_doc = util.load_blob('P21')
    P21 = entity.normalize(wb_doc)

    assert({s.claim.datavalue.id for s in P21.properties['P1629']} ==
           {'Q48277', 'Q290'})

    wb_doc = util.load_blob('Q1700481')
    Q1700481 = entity.normalize(wb_doc)

    assert(Q1700481.properties['P571'][0].claim.datavalue['timestamp'] ==
           '+1883-01-01T00:00:00Z')

    wb_doc = util.load_blob('Q18627581')
    Q18626581 = entity.normalize(wb_doc)

    assert(Q18626581.properties['P106'][0].claim.datavalue['id'] ==
           "Q82594")
