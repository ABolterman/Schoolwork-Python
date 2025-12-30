from CartClass import Cart


class LeastPriorityQueue:

    def __init__(self):
        self._nodes = []

    def __len__(self):
        return len(self._nodes)

    def is_empty(self):
        return len(self._nodes) == 0

    def _upheap(self, index):
        parent_index = self._get_parent_index(index)
        if parent_index is not None and self._nodes[index].__lt__(self._nodes[parent_index]):
            self._nodes[index], self._nodes[parent_index] = self._nodes[parent_index], self._nodes[index]
            self._upheap(parent_index)

    def _get_parent_index(self, index):
        if index == 0:
            return None
        parent_index = (index - 1) // 2
        if parent_index < len(self._nodes):
            return parent_index
        return None

    def add(self, value):
        self._nodes.append(value)
        self._upheap(len(self._nodes) - 1)

    def _get_left_child_index(self, index):
        left_index = (2 * index) + 1
        if left_index < len(self._nodes):
            return left_index
        return None

    def _get_right_child_index(self, index):
        right_index = (2 * index) + 2
        if right_index < len(self._nodes):
            return right_index
        return None

# Adapted from https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
    def __repr__(self, level=0, index=0):
        string = "  " * level + repr(self._nodes[index].num_items)
        print(string)
        left_child_index = self._get_left_child_index(index)
        if left_child_index is not None:
            self.__repr__(level + 1, left_child_index)
        right_child_index = self._get_right_child_index(index)
        if right_child_index is not None:
            self.__repr__(level + 1, right_child_index)
