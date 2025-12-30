class Queue:

    def __init__(self):
        self._storage = []

    def enqueue(self, item):
        self._storage.append(item)

    def dequeue(self):
        return self._storage.pop(0)

    def get_storage_length(self):
        return len(self._storage)