from unittest import TestCase
from BaseShip import Ship, Alignment
from CorvetteClass import Corvette


def create_ships():
    ulysses_expected_name = "Ulysses"
    ulysses_expected_x = 1
    ulysses_expected_y = 2
    ulysses_expected_alignment = Alignment.US
    ulysses_expected_max_health = 20
    ulysses_expected_current_health = 20
    ulysses_expected_range = 25
    ulysses_expected_power = 0
    ulysses_expected_type = Corvette

    ulysses_ship = Corvette(ulysses_expected_name, ulysses_expected_x, ulysses_expected_y, ulysses_expected_alignment)

    odysseus_ship = Ship(ulysses_expected_name, ulysses_expected_x, ulysses_expected_y, ulysses_expected_alignment,
                         ulysses_expected_max_health, ulysses_expected_range, ulysses_expected_power)

    theseus_expected_name = "Theseus"
    theseus_expected_x = 3
    theseus_expected_y = 4
    theseus_expected_alignment = Alignment.THEM
    theseus_expected_max_health = 20
    theseus_expected_current_health = 20
    theseus_expected_range = 10
    theseus_expected_power = 50
    theseus_expected_type = Ship

    theseus_ship = Ship(theseus_expected_name, theseus_expected_x, theseus_expected_y, theseus_expected_alignment,
                        theseus_expected_max_health, theseus_expected_range, theseus_expected_power)

    calypso_expected_name = "Calypso"
    calypso_expected_x = 5
    calypso_expected_y = 6
    calypso_expected_alignment = Alignment.CHAOTIC
    calypso_expected_max_health = 60
    calypso_expected_current_health = 60
    calypso_expected_range = 30
    calypso_expected_power = 15
    calypso_expected_type = Ship

    calypso_ship = Ship(calypso_expected_name, calypso_expected_x, calypso_expected_y, calypso_expected_alignment,
                        calypso_expected_max_health, calypso_expected_range, calypso_expected_power)

    return ulysses_ship, theseus_ship, calypso_ship, odysseus_ship


class TestCorvette(TestCase):
    def test_move(self):
        ulysses_ship, theseus_ship, calypso_ship, odysseus_ship = create_ships()
        ulysses_ship._current_health = 15
        expected_x = 6
        expected_y = 7
        expected_hp = 16

        ulysses_ship.move()
        actual_x = ulysses_ship.get_x()
        actual_y = ulysses_ship.get_y()

        self.assertEqual(expected_hp, ulysses_ship._current_health)
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_attack(self):
        ulysses_ship, theseus_ship, calypso_ship, odysseus_ship = create_ships()
        odysseus_expected_alignment = odysseus_ship.get_alignment()
        theseus_expected_alignment = Alignment.US
        calypso_expected_alignment = calypso_ship.get_alignment()
        theseus_expected_hp = 20

        ulysses_ship.attack(odysseus_ship)
        ulysses_ship.attack(calypso_ship)
        ulysses_ship.attack(theseus_ship)
        odysseus_actual_alignment = odysseus_ship.get_alignment()
        theseus_actual_alignment = theseus_ship.get_alignment()
        calypso_actual_alignment = calypso_ship.get_alignment()
        theseus_actual_hp = theseus_ship._current_health

        self.assertEqual(odysseus_actual_alignment, odysseus_expected_alignment)
        self.assertEqual(calypso_actual_alignment, calypso_expected_alignment)
        self.assertEqual(theseus_actual_hp, theseus_expected_hp)
        self.assertEqual(theseus_actual_alignment, theseus_expected_alignment)
