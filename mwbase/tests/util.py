import json
import os

local_dir = os.path.dirname(os.path.realpath(__file__))


def load_blob(id):
    doc = json.load(open(os.path.join(local_dir, "data/{0}.json".format(id))))
    return list(doc['entities'].values())[0]
