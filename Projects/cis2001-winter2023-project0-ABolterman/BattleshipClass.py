from BaseShip import Ship


class Battleship(Ship):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment, 100, 10, 10)
        self._torpedoes = 10

    def move(self):
        super().move()
        self._x_location -= 1
        self._y_location -= 1

    def attack(self, target):
        # Check if this does damage twice + torpedoes
        if self._torpedoes > 0 & super().attack(target):
            target.assess_damage(10)
            self._torpedoes -= 1

    def status(self):
        stats = super().status()
        stats += f"Torpedoes: {self._torpedoes}"
        return stats
