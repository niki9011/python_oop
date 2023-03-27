class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WokerTests(unittest.TestCase):

    def test_initialization(self):
        worker = Worker("Nikolay Videnov", 5000, 10)
        self.assertEqual(worker.name, "Nikolay Videnov")
        self.assertEqual(worker.salary, 5000)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_rest(self):
        worker = Worker("Nikolay Videnov", 5000, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_not_energy(self):
        worker = Worker("Nikolay Videnov", 5000, -1)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_zerro_energy(self):
        worker = Worker("Nikolay Videnov", 5000, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_energy(self):
        worker = Worker("Nikolay Videnov", 5000, 11)
        worker.work()
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 5000)

    def test_get_info(self):
        worker = Worker("Nikolay Videnov", 5000, 11)
        self.assertEqual(worker.get_info(), f'Nikolay Videnov has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
