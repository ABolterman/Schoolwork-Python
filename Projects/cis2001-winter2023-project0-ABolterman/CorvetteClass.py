from BaseShip import Ship, Alignment


class Corvette(Ship):

    def __init__(self, name, x, y, alignment):
        if alignment == Alignment.CHAOTIC:
            raise Exception("Chaotics can't have Corvettes.")

        super().__init__(name, x, y, alignment, 20, 25, 0)

    def move(self):
        super().move()
        self._x_location += 5
        self._y_location += 5

    def attack(self, target):
        if super().attack(target):
            target.change_alignment()
