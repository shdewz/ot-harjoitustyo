from entities.relic import Relic

from repositories.relic_repository import (
    relic_repository as default_relic_repository
)


class RelicService:
    def __init__(self, relic_repository=default_relic_repository):
        self._relic_repository = relic_repository

    def get_all_relics(self):
        relics = self._relic_repository.find_all()

        return list(relics)


relic_service = RelicService()