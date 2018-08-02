
class AttrDict(dict):

    def __getattr__(self, attr):
        if super().__contains__(attr):
            return super().__getitem__(attr)
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            super().__setattr__(attr, value)
        else:
            super().__setitem__(attr, value)
