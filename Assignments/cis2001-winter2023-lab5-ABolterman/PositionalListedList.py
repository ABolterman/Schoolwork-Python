class PositionalList:

    class Node:

        def __init__(self, item, next=None, previous=None):
            self.item = item
            self.next = next
            self.previous = previous

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.item

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def __init__(self):
        self._front = self.Node(None, None, None)
        self._back = self.Node(None, None, None)
        self._number_of_items = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node.next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._front or node is self._back:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._front.next)

    def last(self):
        return self._make_position(self._back.previous)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.previous)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = self.Node(e, successor, predecessor)
        if predecessor is not None:
            predecessor.next = node
        if successor is not None:
            successor.previous = node
        self._number_of_items += 1
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._front, self._front.next)

    def add_last(self, e):
        return self._insert_between(e, self._back.previous, self._back)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original.previous, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original.next)

    def delete(self, p):
        original = self._validate(p)
        predecessor = original.previous
        successor = original.next
        predecessor.next = successor
        successor.previous = predecessor
        self._number_of_items -= 1
        element = original.item
        original.previous = original.next = original.item = None
        return element

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original.item
        original.item = e
        return old_value

    def __len__(self):
        return self._number_of_items
