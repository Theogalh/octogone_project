from pprint import pprint
from octogone.managers.game_rule import GameRuleManager

game_rule_manager = GameRuleManager()


def subparser_install(subparser):
    parser_game_rule_get_all = subparser.add_parser(
        "get_all",
        help='get all game_rule for one game'
    )
    parser_game_rule_get_all.add_argument("game_id", type=int, help="Game id to game_rule to get")
    parser_game_rule_get_all.set_defaults(func=get_game_rule)

    parser_game_rule_create = subparser.add_parser(
        "create",
        help="create a game_rule"
    )
    parser_game_rule_create.add_argument("game_id", type=int, help="Game id to create game_rule")
    parser_game_rule_create.add_argument("text", type=str, help="text of the game_rule to create")
    parser_game_rule_create.add_argument("ranked", type=bool, help="text of the game_rule to create")
    parser_game_rule_create.set_defaults(func=create_game_rule)


def get_game_rule(game_id):
    game_rules = game_rule_manager.get_all(game_id)
    return game_rules


def create_game_rule(game_id, text, ranked):
    game_rule = game_rule_manager.create(game_id, text, ranked)
    return game_rule
