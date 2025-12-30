from BaseShip import Ship


class Cruiser(Ship):

    def __init__(self, name, x, y, alignment, max_health=50, attack_range=50, attack_power=5):
        super().__init__(name, x, y, alignment, max_health, attack_range, attack_power)

    def move(self):
        super().move()
        self._x_location += 1
        self._y_location += 2

    def attack(self, target):
        super().attack(target)

