from unittest import TestCase
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


class TestShip(TestCase):

    def test_ship_init(self):
        ulysses_ship, theseus_ship, calypso_ship, odysseus_ship = create_ships()
        ulysses_expected_x = 1
        ulysses_expected_y = 2
        ulysses_expected_alignment = Alignment.US
        ulysses_expected_type = Ship
        ulysses_expected_max = 50
        ulysses_expected_current = 50
        ulysses_expected_name = "Ulysses"
        ulysses_expected_status = f"{ulysses_expected_name} \n" \
                                  f"Type: {ulysses_expected_type} \n" \
                                  f"Health: {ulysses_expected_current}/{ulysses_expected_max} \n" \
                                  f"Location: ({ulysses_expected_x}, {ulysses_expected_y} \n"

        ulysses_actual_type = ulysses_ship.get_type()
        ulysses_actual_x = ulysses_ship.get_x()
        ulysses_actual_y = ulysses_ship.get_y()
        ulysses_actual_alignment = ulysses_ship.get_alignment()
        ulysses_actual_status = ulysses_ship.status()

        self.assertEqual(ulysses_actual_type, ulysses_expected_type)
        self.assertEqual(ulysses_actual_x, ulysses_expected_x)
        self.assertEqual(ulysses_actual_y, ulysses_expected_y)
        self.assertEqual(ulysses_actual_alignment, ulysses_expected_alignment)
        self.assertEqual(ulysses_actual_status, ulysses_expected_status)

    #
    def test_assess_damage(self):
        ulysses_ship, theseus_ship, calypso_ship, odysseus_ship = create_ships()
        ulysses_expected_normal_hit = 30
        theseus_expected_below_0 = 0
        calypso_expected_above_max = 60
        calypso_ship._current_health = 50

        ulysses_ship.assess_damage(20)
        ulysses_actual = ulysses_ship._current_health
        theseus_ship.assess_damage(50)
        theseus_actual = theseus_ship._current_health
        calypso_ship.assess_damage(-20)
        calypso_actual = calypso_ship._current_health

        self.assertEqual(ulysses_actual, ulysses_expected_normal_hit)
        self.assertEqual(theseus_actual, theseus_expected_below_0)
        self.assertEqual(calypso_actual, calypso_expected_above_max)

    def test_attack(self):
        ulysses_ship, theseus_ship, calypso_ship, odysseus_ship = create_ships()

        theseus_expected_hp = 0

        # Check for alignment
        self.assertTrue(ulysses_ship.attack(theseus_ship))
        self.assertFalse(ulysses_ship.attack(calypso_ship))
        self.assertFalse(ulysses_ship.attack(odysseus_ship))
        self.assertTrue(theseus_ship.attack(ulysses_ship))
        self.assertTrue(calypso_ship.attack(ulysses_ship))
        self.assertTrue(calypso_ship.attack(theseus_ship))

        # Check for damage and distance calculation
        ulysses_ship.attack(theseus_ship)
        theseus_actual_hp = theseus_ship._current_health
        self.assertEqual(theseus_expected_hp, theseus_actual_hp)
        theseus_ship._x_location = 40
        theseus_ship._y_location = 50
        self.assertFalse(theseus_ship.attack(ulysses_ship))

    def test_move(self):
        ulysses_ship, theseus_ship, calypso_ship, odysseus_ship = create_ships()
        ulysses_ship.assess_damage(2)
        ulysses_expected_hp = 49

        ulysses_ship.move()

        self.assertEqual(ulysses_expected_hp, ulysses_ship._current_health)

    def test_change_alignment(self):
        ulysses_ship, theseus_ship, calypso_ship, odysseus_ship = create_ships()

        ulysses_expected_1 = Alignment.THEM
        ulysses_expected_2 = Alignment.US
        calypso_expected = Alignment.CHAOTIC

        ulysses_ship.change_alignment()
        ulysses_actual_1 = ulysses_ship.get_alignment()
        ulysses_ship.change_alignment()
        ulysses_actual_2 = ulysses_ship.get_alignment()
        calypso_ship.change_alignment()
        calypso_actual = calypso_ship.get_alignment()

        self.assertEqual(ulysses_actual_1, ulysses_expected_1)
        self.assertEqual(ulysses_expected_2, ulysses_actual_2)
        self.assertEqual(calypso_actual, calypso_expected)
