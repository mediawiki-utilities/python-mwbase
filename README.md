# MediaWiki Wikibase

This package provides basic functionality for processing and normalizing
Wikidata Entity JSON.

## Usage

```python
>>> import mwbase
>>> import requests
>>> 
>>> wb_doc = requests.get(
...     "https://wikidata.org/wiki/Special:EntityData/Q42.json").json()
>>> 
>>> entity = mwbase.Entity.from_json(wb_doc['entities']['Q42'])
>>> 
>>> entity.labels['en']
'Douglas Adams'
>>> entity.properties.keys()
dict_keys(['P1273', 'P1411', 'P269', 'P569', 'P950', 'P373', 'P140',
'P2604', 'P2168', 'P2626', 'P3762', 'P244', 'P691', 'P2605', 'P1263',
'P856', 'P108', 'P2019', 'P20', 'P69', 'P1559', 'P40', 'P1695', 'P18',
'P119', 'P106', 'P1953', 'P735', 'P214', 'P26', 'P1442', 'P1303',
'P2048', 'P1816', 'P509', 'P1670', 'P103', 'P349', 'P646', 'P2469',
'P2387', 'P409', 'P800', 'P19', 'P2191', 'P21', 'P2188', 'P2163',
'P910', 'P1477', 'P268', 'P3430', 'P3106', 'P434', 'P271', 'P22',
'P1003', 'P1617', 'P551', 'P949', 'P1006', 'P1015', 'P2611', 'P1417',
'P3373', 'P2963', 'P1207', 'P31', 'P866', 'P1266', 'P1233', 'P1258',
'P1005', 'P1284', 'P1196', 'P906', 'P734', 'P25', 'P998', 'P227',
'P947', 'P1315', 'P535', 'P3417', 'P648', 'P570', 'P172', 'P1415',
'P1368', 'P2435', 'P27', 'P396', 'P1375', 'P1412', 'P345', 'P3222',
'P213'])
>>> entity.sitelinks.keys()
dict_keys(['shwiki', 'eswikiquote', 'ruwikiquote', 'ruwiki',
'itwikiquote', 'bewiki', 'mgwiki', 'hewikiquote', 'frwiki',
'arzwiki', 'gawiki', 'cswikiquote', 'fawikiquote', 'huwikiquote',
'elwiki', 'jvwiki', 'rowiki', 'etwiki', 'huwiki', 'ukwiki',
'azwiki', 'trwiki', 'bgwikiquote', 'kowiki', 'euwiki', 'nlwikiquote',
'mkwiki', 'plwiki', 'dawiki', 'dewiki', 'eowikiquote', 'svwiki',
'zhwiki', 'cawiki', 'tawiki', 'idwiki', 'mlwiki', 'nnwiki', 'eswiki',
'viwiki', 'frwikiquote', 'lawiki', 'bswiki', 'enwiki', 'scwiki',
'enwikiquote', 'elwikiquote', 'fiwiki', 'mrwiki', 'fiwikiquote',
'simplewiki', 'jawiki', 'scowiki', 'be_x_oldwiki', 'iswiki',
'zhwikiquote', 'nowiki', 'etwikiquote', 'fawiki', 'arwiki',
'plwikiquote', 'lvwiki', 'bnwiki', 'bgwiki', 'slwiki', 'cywiki',
'iowiki', 'astwiki', 'kawiki', 'hewiki', 'barwiki', 'bswikiquote',
'dewikiquote', 'ltwikiquote', 'vepwiki', 'hywikiquote', 'ocwiki',
'mrjwiki', 'skwiki', 'ptwikiquote', 'ptwiki', 'glwikiquote',
'liwikiquote', 'glwiki', 'warwiki', 'trwikiquote', 'srwiki',
'azwikiquote', 'itwiki', 'thwikiquote', 'svwikiquote', 'hywiki',
'eowiki', 'cswiki', 'sqwiki', 'urwiki', 'simplewikiquote',
'skwikiquote', 'hrwiki', 'nlwiki'])
```
