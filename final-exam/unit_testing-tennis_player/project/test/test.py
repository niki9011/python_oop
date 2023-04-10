from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.tennis = TennisPlayer("Niki", 32, 100.0)

    def test_initialization(self):
        self.assertEqual(self.tennis.name, "Niki")
        self.assertEqual(self.tennis.age, 32)
        self.assertEqual(self.tennis.points, 100.0)
        self.assertEqual(self.tennis.wins, [])

    def test_name_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            tennis = TennisPlayer("Ni", 32, 100.0)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_name_valid(self):
        self.tennis.name = "Niki"
        assert self.tennis.name == "Niki"

    def test_age_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            tennis = TennisPlayer("Niki", 17, 100.0)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_existing(self):
        self.tennis.wins.append("Bobi Ivanov")
        self.assertEqual(self.tennis.add_new_win("Bobi Ivanov"), "Bobi Ivanov has been already added to the list of wins!")
        self.assertEqual(self.tennis.wins, ["Bobi Ivanov"])

    def test_add_actor_valid(self):
        self.tennis.add_new_win("Bobi Ivanov")
        self.assertEqual(self.tennis.wins, ["Bobi Ivanov"])

    def test__lt__method_other_higher_rating(self):
        tesnnis2 = TennisPlayer("Asen Filipov", 36, 105.0)
        result = self.tennis < tesnnis2
        self.assertEqual("Asen Filipov is a top seeded player and he/she is better than Niki", result)


    def test_lt_method_self_higher_rating(self):
        tennis1 = TennisPlayer("Bobi Malinov", 35, 101.0)
        result = self.tennis > tennis1
        self.assertEqual("Bobi Malinov is a better player than Niki", result)

    def test_str(self):
        self.tennis.add_new_win("Asen Filipov")
        self.tennis.add_new_win("Bobi Malinov")
        self.assertEqual(self.tennis.__str__(), "Tennis Player: Niki\n"
                                                "Age: 32\n"
                                                "Points: 100.0\n"
                                                "Tournaments won: Asen Filipov, Bobi Malinov")


if __name__ == '__main__':
    unittest.main()
