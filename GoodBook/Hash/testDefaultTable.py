class TestDefaultTable:

    def __init__(self):
        self._table = 10 * [None]



    def copyng(self):
        test = [1, 2, 3, 4, 5]
        for k in test:
            self[k] = k
