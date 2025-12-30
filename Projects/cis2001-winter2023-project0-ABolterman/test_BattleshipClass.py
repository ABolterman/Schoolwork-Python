from unittest import TestCase
from BattleshipClass import Battleship
from BaseShip import Ship, Alignment


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
    calypso_expected_max_health = 100
    calypso_expected_current_health = 100
    calypso_expected_range = 10
    calypso_expected_power = 10
    calypso_expected_type = Battleship
    calypso_expected_torpedoes = 10

    calypso_ship = Battleship(calypso_expected_name, calypso_expected_x, calypso_expected_y, calypso_expected_alignment)

    return ulysses_ship, calypso_ship


class TestBattleship(TestCase):

    def test_status(self):
        ulysses_ship, calypso_ship = create_ships()
        calypso_expected_name = "Calypso"
        calypso_expected_x = 5
        calypso_expected_y = 6
        calypso_expected_type = Battleship
        calypso_expected_max_health = 100
        calypso_expected_current_health = 100
        calypso_expected_torpedoes = 10

        calypso_expected_status = f"{calypso_expected_name} \n" \
                                  f"Type: {calypso_expected_type} \n" \
                                  f"Health: {calypso_expected_current_health}/{calypso_expected_max_health} \n" \
                                  f"Location: ({calypso_expected_x}, {calypso_expected_y} \n" \
                                  f"Torpedoes: {calypso_expected_torpedoes}"

        calypso_actual_status = calypso_ship.status()

        self.assertEqual(calypso_actual_status, calypso_expected_status)

    def test_move(self):
        ulysses_ship, calypso_ship = create_ships()
        calypso_ship._current_health = 95
        expected_x = 4
        expected_y = 5
        expected_hp = 96

        calypso_ship.move()
        actual_x = calypso_ship.get_x()
        actual_y = calypso_ship.get_y()

        self.assertEqual(expected_hp, calypso_ship._current_health)
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_attack(self):
        ulysses_ship, calypso_ship = create_ships()

        ulysses_expected_hp = 30
        calypso_expected_torps = 9
        ulysses_expected_hp2 = 20

        calypso_ship.attack(ulysses_ship)
        ulysses_actual_hp = ulysses_ship._current_health
        calypso_actual_torps = calypso_ship._torpedoes

        self.assertEqual(ulysses_expected_hp, ulysses_actual_hp)
        self.assertEqual(calypso_expected_torps, calypso_actual_torps)

        # Test number of torpedoes
        calypso_ship._torpedoes = 0

        calypso_ship.attack(ulysses_ship)
        ulysses_actual_hp2 = ulysses_ship._current_health

        self.assertEqual(ulysses_expected_hp2, ulysses_actual_hp2)
