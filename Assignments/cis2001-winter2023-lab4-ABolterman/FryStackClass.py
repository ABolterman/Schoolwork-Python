class FryStack:

    class Fry:
        def __init__(self):
            self.age = 0

        def age_fry(self):
            self.age += 1

        def get_fry_age(self):
            return self.age

    def __init__(self):
        self.storage = []
        self.cooking = []

    def push(self):
        self.storage.append(self.Fry())

    def pop(self):
        self.storage.pop()

    def peek_stack(self):
        return self.storage[-1].age

    def get_length(self):
        return len(self.storage)

    def age_fries(self):
        for i in range(len(self.storage)):
            self.storage[i].age_fry()

    def drop_fries(self, cost, queue, time):
        if len(self.cooking) == 0 and ((self.get_length() < 4 and queue.get_length != 0) or self.get_length() == 0):
            self.cooking.append(self.Fry)
            self.cooking.append(self.Fry)
            self.cooking.append(self.Fry)
            self.cooking.append(self.Fry)
            cost += 2
            time = 0
        return cost, time

    def cooking_done(self, time):
        if time == 2:
            for i in range(4):
                if self.get_length() < 8:
                    self.push()
                self.cooking.pop()


