#
#
#
from collections import UserDict


class BidirectionalDict(UserDict):
    # bd['a'] = 'b'
    # a -> b, b -> a

    # del bd['a']
    # a -> b and b -> a are removed

    # bd['a'] = 'v'
    # a -> v, v -> a

    def __setitem__(self, key, value):
        if key in self:
            del self[key]

        if value in self:
            del self[value]

        super().__setitem__(key, value)
        super().__setitem__(value, key)

    def __delitem__(self, key):
        super().__delitem__(self[key])
        super().__delitem__(key)

    def __len__(self):
        return super().__len__() // 2
