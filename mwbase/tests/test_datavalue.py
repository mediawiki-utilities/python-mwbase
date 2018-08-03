from ..datavalue import normalize


def test_string():
    string = normalize({
        'type': "string",
        'value': "I have a lovely bunch of coconuts"
    })

    assert str(string) == "'I have a lovely bunch of coconuts'"


def test_quantity():
    quantity = normalize({
        'type': "quantity",
        'value': {
            'amount': "+5",
            'upperBound': "+5",
            'lowerBound': "+5",
            'unit': "1"
        }
    })

    assert str(quantity) == "5 (5-5) 1"


def test_entity_id():
    entity_id = normalize({
        "value": {
            "entity-type": "item",
            "numeric-id": 6636
        },
        "type": "wikibase-entityid"
    })

    assert str(entity_id) == "Q6636"


def test_time():
    entity_id = normalize({
        "value": {
            "time": "+1931-00-00T00:00:00Z",
            "timezone": 0,
            "before": 0,
            "after": 0,
            "precision": 9,
            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
        },
        "type": "time"
    })

    assert str(entity_id) == "+1931-00-00T00:00:00Z"


def test_coordinate():
    coordinate = normalize({
        'type': "globecoordinate",
        'value': {
            'latitude': 50,
            'longitude': -50,
            'altitude': 10,
            'precision': 0,
            'globe': "https://www.wikidata.org/wiki/Q2"
        }
    })

    assert str(coordinate) == \
        "50 x -50 x 10 @ https://www.wikidata.org/wiki/Q2"
