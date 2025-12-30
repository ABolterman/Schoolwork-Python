import random


class CarQueue:

    class Car:
        def __init__(self):
            self._order = random.randint(1, 6)

    def __init__(self):
        self.storage = []

    def enqueue(self):
        self.storage.append(self.Car())

    def dequeue(self):
        self.storage.pop(0)

    def get_order(self):
        return self.storage[0]._order

    def decrease_order(self):
        self.storage[0]._order -= 1

    def get_length(self):
        return len(self.storage)
