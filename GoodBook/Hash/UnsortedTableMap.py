from GoodBook.Hash.MapBase import MapBase

class UnsortedTableMap(MapBase):

    def __init__(self):
        self._table = []


    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value

        raise KeyError('Key Error: ' + repr(k))
    def __setitem__(self, key, value):


    def __delitem__(self, key):

    def __len__(self):

    def __iter__(self):