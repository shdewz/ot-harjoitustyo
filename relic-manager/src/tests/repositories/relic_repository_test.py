import unittest
from repositories.relic_repository import relic_repository
from entities.relic import Relic


class TestTodoRepository(unittest.TestCase):
    def setUp(self):
        relic_repository.delete_all()

        self.relic_a = Relic(1, "Example Set 1", "Head", 15, "HP", [("SPD", 6.2), ("ATK%", 8.7), ("EHR%", 11.9), ("ATK", 76)])
        self.relic_b = Relic(1, "Example Set 2", "Body", 15, "ATK", [("EHR%", 7.8), ("CDMG", 5.8), ("BE%", 12.9), ("HP", 74)])

    def test_create(self):
        relic_repository.create(self.relic_a)
        relics = relic_repository.find_all()

        self.assertEqual(len(relics), 1)
        self.assertEqual(relics[0].relic_set, self.relic_a.relic_set)

    def test_find_all(self):
        relic_repository.create(self.relic_a)
        relic_repository.create(self.relic_b)
        relics = relic_repository.find_all()

        self.assertEqual(len(relics), 2)
        self.assertEqual(relics[0].relic_set, self.relic_a.relic_set)
        self.assertEqual(relics[1].relic_set, self.relic_b.relic_set)

    def test_delete(self):
        relic = relic_repository.create(self.relic_a)
        relics = relic_repository.find_all()

        self.assertEqual(len(relics), 1)

        relic_repository.delete(relic.relic_id)

        relics = relic_repository.find_all()

        self.assertEqual(len(relics), 0)