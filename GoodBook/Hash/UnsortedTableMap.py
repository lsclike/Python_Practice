from GoodBook.Hash.MapBase import MapBase


class UnsortedTableMap(MapBase):

    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        for item in self._table:
            if key == item._key:
                return item._value

        raise KeyError('Key Error: ' + repr(key))

    def __setitem__(self, key, value):
        for item in self._table:
            if key == item._key:
                item._value = value
                return

        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        for n in range(len(self._table)):
            if self._table[n]._key == key:
                self._table.pop(n)
                return

        raise KeyError('Key Error: ' + repr(key))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield (item._key, item._value)