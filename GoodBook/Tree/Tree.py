class Tree:

    class Position:

        def element(self):
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            return not self.__eq__(other)

    def root(self):
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('Must be implemented by subclass')

    def is_root(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def is_leaf(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def is_empty(self):
        return len(self) == 0

    def positions(self):
        return self.preorder()

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p


