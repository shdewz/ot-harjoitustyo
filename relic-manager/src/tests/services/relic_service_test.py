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
    
    def delete(self, id):
        self.relics = list(filter(lambda x: x.id != id, self.relics))
        return True


class TestRelicService(unittest.TestCase):
    def setUp(self):
        self.relic_service = RelicService(FakeRelicRepository())


    def test_create_relic(self):
        self.relic_service.create(1, "Example Set", "Head", 15, "HP", [("SPD", 6.2), ("ATK%", 8.7), ("EHR%", 11.9), ("ATK", 76)])
        relics = self.relic_service.get_all()

        self.assertEqual(len(relics), 1)
        self.assertEqual(relics[0].level, 15)
        self.assertEqual(relics[0].relic_type, "Head")
        self.assertAlmostEqual(int(relics[0].mainstat_value), 705)

    def test_delete_relic(self):
        self.relic_service.create(1, "Example Set", "Head", 15, "HP", [("SPD", 6.2), ("ATK%", 8.7), ("EHR%", 11.9), ("ATK", 76)])
        relics = self.relic_service.get_all()
        self.assertEqual(len(relics), 1)

        self.relic_service.delete(1)
        relics = self.relic_service.get_all()
        self.assertEqual(len(relics), 0)
        
