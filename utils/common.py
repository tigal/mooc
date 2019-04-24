# -*- coding: utf-8 -*-

from collections import OrderedDict


class BeautyOrderedDict(OrderedDict):

    def __init__(self, *args, **kwargs):
        super(BeautyOrderedDict, self).__init__(*args, **kwargs)
        self.make_attr_keys()

    def make_attr_keys(self):
        for key in list(self.keys()):
            setattr(self, key.upper(), key)

    def items_raw(self):
        return list(self.items())

    def __getattr__(self, attr):
        if attr in self.__dict__ or attr in self.keys():
            return self.get(attr, None)
        else:
            raise AttributeError(attr)
