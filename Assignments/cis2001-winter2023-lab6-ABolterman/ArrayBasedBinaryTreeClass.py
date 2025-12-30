class ArrayBasedBinaryTree:

    def __init__(self, values=None):
        self.nodes = []
        if values is not None:
            for value in values:
                self.add_node(value)

    def add_node(self, value):
        self.nodes.append(value)

    def get_node(self, p):
        if p < len(self.nodes):
            return self.nodes[p]

    def left(self, p):
        left_child = 2 * p + 1
        if left_child < len(self.nodes):
            return left_child
        else:
            return None

    def right(self, p):
        right_child = 2 * p + 2
        if right_child < len(self.nodes):
            return right_child
        else:
            return None

    def get_sibling(self, p):
        if p == 0:
            return None
        if p % 2 == 1 and p + 1 < len(self.nodes):
            return p + 1
        return p - 1

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
