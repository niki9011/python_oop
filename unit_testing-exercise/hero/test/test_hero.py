import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Batman", 1, 100, 100)
        self.enemy = Hero("Robin", 1, 50, 50)

    def test_initialization_valid(self):
        self.assertEqual("Batman", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_hero_whit_enemy(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_health_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_health_zero_enemy(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight Robin. He needs to rest", str(ve.exception))

    def test_health_hero_and_enemy_zero(self):
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.damage

        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual(result, "Draw")

    def test_enemy_hero_health_zero(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_hero_health_zero(self):
        self.hero, self.enemy = self.enemy, self.hero
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test__str__(self):
        self.assertEqual(f"Hero Batman: 1 lvl\n" +
                         "Health: 100\n" +
                         "Damage: 100\n", str(self.hero))


if __name__ == '__main__':
    unittest.main()
