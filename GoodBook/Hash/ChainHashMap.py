from GoodBook.Hash.HashMapBase import HashMapBase
from GoodBook.Hash.UnsortedTableMap import UnsortedTableMap


class ChainHashMap(HashMapBase):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if not self._table[j]:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if (oldsize < len(self._table[j])):
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for item in bucket:
                    yield item


if __name__ == '__main__':
    testChainHashMap = ChainHashMap()
    testChainHashMap['abc'] = 123
    testChainHashMap['cba'] = 321
    print(len(testChainHashMap))
    for (k, v) in testChainHashMap:
        print(f'key is {k}, value is {v}')