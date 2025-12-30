import math
from enum import Enum


class Alignment(Enum):
    US = 1
    THEM = 2
    CHAOTIC = 3


class Ship:

    def __init__(self, name, x, y, alignment, max_health, attack_range, attack_power):
        self._name = name
        self._alignment = alignment
        self._x_location = x
        self._y_location = y
        self._attack_range = attack_range
        self._attack_power = attack_power
        self._current_health = max_health
        self._max_health = max_health

    def attack(self, target):
        ship_alignment = self.get_alignment()
        target_alignment = target.get_alignment()
        if ship_alignment is Alignment.CHAOTIC or \
                ((ship_alignment == Alignment.US and target_alignment == Alignment.THEM) or
                 (ship_alignment == Alignment.THEM and target_alignment == Alignment.US)):
            distance = math.sqrt((self.get_x() - target.get_x()) ** 2 + (self.get_y() - target.get_y()) ** 2)
            if distance <= self._attack_range:
                target.assess_damage(self._attack_power)
                return True
            else:
                return False
        else:
            return False

    def get_type(self):
        return self.__class__

    def get_x(self):
        return self._x_location

    def get_y(self):
        return self._y_location

    def get_alignment(self):
        return self._alignment

    def status(self):
        stats = f"{self._name} \n" \
                f"Type: {self.get_type()} \n" \
                f"Health: {self._current_health}/{self._max_health} \n" \
                f"Location: ({self._x_location}, {self._y_location} \n"
        return stats

    def move(self):
        self.assess_damage(-1)

    def change_alignment(self):
        if self._alignment == Alignment.US:
            self._alignment = Alignment.THEM
        elif self._alignment == Alignment.THEM:
            self._alignment = Alignment.US

    def assess_damage(self, amount):
        self._current_health -= amount
        if self._current_health < 0:
            self._current_health = 0
        if self._current_health > self._max_health:
            self._current_health = self._max_health
