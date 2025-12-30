import random


class Cart:
    def __init__(self, num):
        self.num_items = random.randint(0, 50)

    def __lt__(self, other):
        return self.num_items <= 15 and other.num_items > 15

    def __gt__(self, other):
        return self.num_items > 15 and other.num_items <= 15

    def __eq__(self, other):
        return self.num_items <= 15 and other.num_items <= 15

    def get_items(self):
        return str(self.num_items)

