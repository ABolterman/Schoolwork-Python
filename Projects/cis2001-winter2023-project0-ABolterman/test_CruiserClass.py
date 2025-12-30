from unittest import TestCase
from BaseShip import Ship, Alignment
from CruiserClass import Cruiser


def create_ships():
    ulysses_expected_name = "Ulysses"
    ulysses_expected_x = 1
    ulysses_expected_y = 2
    ulysses_expected_alignment = Alignment.US
    ulysses_expected_max_health = 50
    ulysses_expected_current_health = 50
    ulysses_expected_range = 20
    ulysses_expected_power = 25
    ulysses_expected_type = Ship

    ulysses_ship = Ship(ulysses_expected_name, ulysses_expected_x, ulysses_expected_y, ulysses_expected_alignment,
                        ulysses_expected_max_health, ulysses_expected_range, ulysses_expected_power)

    calypso_expected_name = "Calypso"
    calypso_expected_x = 5
    calypso_expected_y = 6
    calypso_expected_alignment = Alignment.CHAOTIC
    calypso_expected_max_health = 50
    calypso_expected_current_health = 50
    calypso_expected_range = 50
    calypso_expected_power = 5
    calypso_expected_type = Cruiser

    calypso_ship = Cruiser(calypso_expected_name, calypso_expected_x, calypso_expected_y, calypso_expected_alignment)

    return ulysses_ship, calypso_ship


class TestCruiser(TestCase):
    def test_attack(self):
        ulysses_ship, calypso_ship = create_ships()
        ulysses_expected_hp = 45

        calypso_ship.attack(ulysses_ship)
        ulysses_actual_hp = ulysses_ship._current_health

        self.assertEqual(ulysses_expected_hp, ulysses_actual_hp)

    def test_move(self):
        ulysses_ship, calypso_ship = create_ships()
        expected_x = 6
        expected_y = 8
        calypso_ship._current_health = 45
        expected_hp = 46

        calypso_ship.move()
        actual_x = calypso_ship.get_x()
        actual_y = calypso_ship.get_y()

        self.assertEqual(expected_hp, calypso_ship._current_health)
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
