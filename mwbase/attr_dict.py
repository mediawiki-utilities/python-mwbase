class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)

    def __getattr__(self, attr):
        if attr not in self:
            raise AttributeError(attr)
        else:
            return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value
