class Stack:
    def __init__(self):
        self._storage = []

    def push(self,item):
        self._storage.append(item)

    def pop(self):
        return self._storage.pop()

    def get_storage_length(self):
        return len(self._storage)