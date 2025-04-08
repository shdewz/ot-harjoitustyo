from entities.relic import Relic
from repositories.relic_repository import relic_repository as default_relic_repository


class RelicService:
    def __init__(self, relic_repository=default_relic_repository):
        self._relic_repository = relic_repository

    def get_all(self):
        relics = self._relic_repository.find_all()

        return list(relics)

    def create(self, id, relic_set, relic_type, level, mainstat, substats):
        relic = Relic(id, relic_set, relic_type, level, mainstat, substats)
        return self._relic_repository.create(relic)
    
    def delete(self, id):
        return self._relic_repository.delete(id)


relic_service = RelicService()
