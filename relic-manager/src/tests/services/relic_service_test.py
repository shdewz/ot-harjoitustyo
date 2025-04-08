import unittest
from services.relic_service import RelicService
from entities.relic import Relic


class FakeRelicRepository:
    def __init__(self, relics=None):
        self.relics = relics or []

    def find_all(self):
        return self.relics
    
    def create(self, relic):
        self.relics.append(relic)
        return relic


class TestRelicService(unittest.TestCase):
    def setUp(self):
        self.relic_service = RelicService(FakeRelicRepository())

        self.relic_a = Relic(1, "Example Set", "Head", 15, "HP", [("SPD", 6.2), ("ATK%", 8.7), ("EHR%", 11.9), ("ATK", 76)])
        self.relic_b = Relic(2, "Example Set", "Body", 15, "CDMG", [("SPD", 6.2), ("ATK%", 8.7), ("EHR%", 11.9), ("ATK", 76)])

    def test_create_relic(self):
        self.relic_service.create(1, "Example Set", "Head", 15, "HP", [("SPD", 6.2), ("ATK%", 8.7), ("EHR%", 11.9), ("ATK", 76)])
        relics = self.relic_service.get_all()

        self.assertEqual(len(relics), 1)
        self.assertEqual(relics[0].level, 15)
        self.assertEqual(relics[0].relic_type, "Head")
        self.assertAlmostEqual(relics[0].mainstat_value, 705)
