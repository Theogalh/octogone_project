from octogone.managers.base_manager import BaseManager
from octogone.models import Season


class SeasonManager(BaseManager):
    """
    Manager class for Seasons
    This class handles all the Seasons' methods
    """

    model = Season

    def create(self, name):
        if self.model.query.filter_by(name=name).first():
            raise ValueError
        season = self.model.create(name)
        return season