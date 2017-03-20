import mwbase
import requests

wb_doc = requests.get(
    "https://wikidata.org/wiki/Special:EntityData/Q42.json").json()

entity = mwbase.Entity.from_json(wb_doc['entities']['Q42'])

entity.labels['en']
entity.claims.keys()
entity.sitelinks.keys()
