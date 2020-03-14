from octogone.managers.base_manager import BaseManager
from octogone.models import Game


class GameManager(BaseManager):
    """
    Manager class for Games
    This class handles all the Games' methods
    """

    model = Game

    def create(self, name):
        if self.model.query.filter_by(name=name).first():
            raise ValueError
        game = self.model.create(name)
        return game

    def delete(self, id):
        game = self.model.query.get(id)
        if game:
            game.remove()
        else:
            raise ValueError
