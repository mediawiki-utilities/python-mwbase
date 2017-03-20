from nose.tools import eq_

from . import util
from .. import entity


def test_normalize():
    wb_doc = util.load_blob('Q7251')
    Q7251 = entity.normalize(wb_doc)

    eq_(Q7251.claims['P268'][0]['statement']['datavalue']['value'],
        "12205670t")

    eq_({pid for pid, claims in Q7251.claims.items() if len(claims) > 1},
        {'P1343', 'P800', 'P512', 'P101', 'P108', 'P69', 'P106', 'P19',
         'P166'})

    eq_(Q7251.claims['P21'][0]['statement']['datavalue']['id'],
        "Q6581097")

    eq_({(pid, refs[0]['datavalue']['type'])
         for pid, refs in Q7251.claims['P21'][0]['references'].items()},
        {('P143', 'wikibase-entityid'),
         ('P813', 'time'),
         ('P248', 'wikibase-entityid')})

    wb_doc = util.load_blob('P21')
    P21 = entity.normalize(wb_doc)

    eq_({c['statement']['datavalue']['id'] for c in P21.claims['P1629']},
        {'Q48277', 'Q290'})

    wb_doc = util.load_blob('Q1700481')
    Q1700481 = entity.normalize(wb_doc)

    eq_(Q1700481.claims['P571'][0]['statement']['datavalue']['timestamp'],
        '+1883-01-01T00:00:00Z')

    wb_doc = util.load_blob('Q18627581')
    Q18626581 = entity.normalize(wb_doc)

    eq_(Q18626581.claims['P106'][0]['statement']['datavalue']['id'],
        "Q82594")
