from GoodBook.Hash.HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):

    _AVAIL = object()

    def _is_available(self, j):
        return self._table(j) is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        first_available = None
        while True:
            if self._is_available(j):
                if first_available is None:
                    first_available = j
                if self._table[j] is None:
                    return False, first_available

            elif k == self._table[j]._key:
                return True, j

            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        result, index = self._find_slot(j, k)
        if not result:
            raise KeyError('No such a key' + repr(k))
        return self._table[index]._value

    def _bucket_setitem(self, j, k, v):
        result, index = self._find_slot(j, k)
        if not result:
            self._table[index] = self._Item(k, v)
            self._n += 1
        else:
            self._table[index]._value = v

    def _bucket_delitem(self, j, k):
        result, index = self._find_slot(j, k)
        if not result:
            raise KeyError('No such a key', repr(k))
        self._table[index] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key




