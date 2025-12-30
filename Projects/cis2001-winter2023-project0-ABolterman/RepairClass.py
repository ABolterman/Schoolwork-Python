from CruiserClass import Cruiser
from BaseShip import Alignment


class Repair(Cruiser):

    def __init__(self, name, x, y, alignment):
        if alignment == Alignment.CHAOTIC:
            raise Exception("Chaotics can't have Repair.")
        super().__init__(name, x, y, alignment, 20, 25, -1000)

    def attack(self, target):
        self.change_alignment()
        super().attack(target)
        self.change_alignment()
