from entities.relic import Relic
from repositories.relic_repository import relic_repository as default_relic_repository


class RelicService:
    """Class for handling relic operations
    """

    def __init__(self, relic_repository=default_relic_repository):
        """Constructor

        Args:
            relic_repository: a RelicRepository object 
        """

        self._relic_repository = relic_repository

    def get_all(self):
        """Returns all relics in the database

        Returns:
            Returns a list of Relic objects
        """

        relics = self._relic_repository.find_all()

        return list(relics)

    def create(self, relic_set, relic_type, level, mainstat, substats):
        """Creates a relic

        Args:
            relic_set: String, Relic set name
            relic_type: String, Type of relic (Head, Hands, Body, Feet, Ball, Rope)
            level: Int, Relic level (1-15)
            mainstat: String, Relic mainstat type
            substats: List of substat type-value pairs

        Returns:
            Returns a Relic object that the repository provides
        """

        relic = Relic(-1, relic_set, relic_type, level, mainstat, substats)
        return self._relic_repository.create(relic)

    def delete(self, relic_id):
        return self._relic_repository.delete(relic_id)


relic_service = RelicService()
