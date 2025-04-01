import unittest
from entities.relic import Relic
from services.relic_service import RelicService


class FakeRelicRepository:
    def __init__(self, relics=None):
        self.relics = relics or []

    def get_all(self):
        return self.relics
    
    def create(self, relic):
        self.relics.append(relic)
        return relic


class TestRelicService(unittest.TestCase):
    def setUp(self):
        self.relic_service = RelicService(FakeRelicRepository())

        self.relic_a = Relic(1, "set 1", "head", 15, "hp", [("spd", 6.2)])
        self.relic_b = Relic(2, "set 5", "body", 15, "atk%", [("atk", 78)])

    def test_create_relic(self):
        self.relic_service.create(self.relic_a)
        relics = self.relic_service.get_all()

        self.assertEqual(len(relics), 1)
        self.assertEqual(relics[0].level, 15)
        self.assertEqual(relics[0].type, "head")
