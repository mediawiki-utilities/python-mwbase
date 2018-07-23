from collections import OrderedDict


class AttrDict(OrderedDict):
    def __init__(self, *args, **kwargs):
        super(OrderedDict, self).__init__(*args, **kwargs)

    def __getattribute__(self, attr):
        if attr in self:
            return self[attr]
        else:
            return super(OrderedDict, self).__getattribute__(attr)

    def __setattr__(self, attr, value):
        self[attr] = value
