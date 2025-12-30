from unittest import TestCase
from BaseShip import Ship, Alignment
from RepairClass import Repair


def create_ships():
    ulysses_expected_name = "Ulysses"
    ulysses_expected_x = 1
    ulysses_expected_y = 2
    ulysses_expected_alignment = Alignment.US
    ulysses_expected_max_health = 20
    ulysses_expected_current_health = 20
    ulysses_expected_range = 25
    ulysses_expected_power = -1000
    ulysses_expected_type = Repair

    ulysses_ship = Repair(ulysses_expected_name, ulysses_expected_x, ulysses_expected_y, ulysses_expected_alignment)

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


class TestRepair(TestCase):

    def test_attack(self):
        ulysses_ship, theseus_ship, calypso_ship, odysseus_ship = create_ships()
        odysseus_ship._current_health = 1
        odysseus_expected = 20

        ulysses_ship.attack(odysseus_ship)
        odysseus_actual = odysseus_ship._current_health

        self.assertFalse(ulysses_ship.attack(theseus_ship))
        self.assertFalse(ulysses_ship.attack(calypso_ship))

        self.assertEqual(odysseus_actual, odysseus_expected)
