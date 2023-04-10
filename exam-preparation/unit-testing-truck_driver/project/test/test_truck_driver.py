import unittest
from python_oop.FINAL_EXAM.project import TruckDriver


class TestTruckDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Jon", 1)

    def test__int__(self):
        driver = TruckDriver("Jon", 1)
        assert self.driver.name == "Jon"
        assert self.driver.money_per_mile == 1
        assert isinstance(self.driver.available_cargos, dict)
        assert not self.driver.available_cargos
        assert self.driver.earned_money == 0
        assert self.driver.miles == 0

    def test_set_earned_money_not_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -3

            assert ex.exception.args[0] == "Jon went bankrupt."

        # self.assertEqual("Jon went bankrupt.", str(ex.exception))

        assert ex.exception.args[0] == "Jon went bankrupt."

    def test_set_earned_money_valid(self):
        assert self.driver.earned_money == 0
        self.driver.earned_money = 5
        assert self.driver.earned_money == 5

        # self.driver.earned_money = 0
        # self.driver.earned_money += 6
        # self.assertEqual(6, self.driver.earned_money)

    def test_add_cargo_offer_rais_exception(self):
        self.driver.add_cargo_offer("Paris", 15)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Paris", 13)

        assert ex.exception.args[0] == "Cargo offer is already added."

        # self.driver.add_cargo_offer("Paris", 15)
        #
        # with self.assertRaises(Exception) as ex:
        #     self.driver.add_cargo_offer("Paris", 16)
        # self.assertEqual(f"Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_valid(self):
        result = self.driver.add_cargo_offer("Paris", 15)
        assert result == f"Cargo for 15 to Paris was added as an offer."
        # self.assertEqual(f"Cargo for 15 to Paris was added as an offer.", result)

    def test_drive_best_cargo_offer_no_offer_raises_exception(self):
        assert not self.driver.available_cargos


        res = self.driver.drive_best_cargo_offer()

        assert res == "There are no offers available."

        assert self.driver.earned_money == 0
        assert self.driver.miles == 0

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("Paris", 15)
        self.driver.add_cargo_offer("London", 25)
        self.driver.add_cargo_offer("Sofia", 8)

        assert self.driver.earned_money == 0
        assert self.driver.miles == 0
        res = self.driver.drive_best_cargo_offer()

        assert res == f"Jon is driving 25 to London."

    def test_eat(self):
        self.driver.earned_money = 50

        self.driver.eat(250)
        assert self.driver.earned_money == 30

    def test_sleep(self):
        self.driver.earned_money = 50

        self.driver.sleep(1000)
        assert self.driver.earned_money == 5

    def test_pump_gas(self):
        self.driver.earned_money = 550

        self.driver.pump_gas(1500)
        assert self.driver.earned_money == 50

    def test_repair_truck(self):
        self.driver.earned_money = 7500

        self.driver.repair_truck(10000)
        assert self.driver.earned_money == 0

    def test__repr__(self):
        res = str(self.driver)
        res_repr = repr(self.driver)

        assert res == res_repr
        assert res == f"Jon has 0 miles behind his back."

    def test_check_for_activities(self):
        self.driver.earned_money = 11760

        res = self.driver.check_for_activities(10000)
        assert res is None

        assert self.driver.earned_money == 10

    def test_drive_best_offer_with_activities(self):
        self.driver.earned_money = 11760 - 10011

        needed_money_cargo = 11750
        km_to_drive = 10000
        money_to_earn = self.driver.money_per_mile * km_to_drive

        self.driver.add_cargo_offer("Milano", 10000)
        with self.assertRaises(ValueError) as ex:
            self.driver.drive_best_cargo_offer()

        assert ex.exception.args[0] == "Jon went bankrupt."



if __name__ == '__main__':
    unittest.main()
