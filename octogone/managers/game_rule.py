from octogone.managers.base_manager import BaseManager
from octogone.models import GameRule


class GameRuleManager(BaseManager):
    """
    Manager class for GameRules
    This class handles all the GameRules' methods
    """

    model = GameRule

    def get_all(self, game_id):
        return self.model.query.filter_by(game_id=game_id).all()

    def create(self, game_id, text, ranked):
        game_rule = self.model.create(game_id, text, ranked)
        return game_rule
