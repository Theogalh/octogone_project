from pprint import pprint
from octogone.managers.game import GameManager

game_manager = GameManager()

def subparser_install(subparser):
    parser_game_get_all = subparser.add_parser(
        "get_all",
        help='get all games'
    )
    parser_game_get_all.set_defaults(func=get_game)

    parser_game_create = subparser.add_parser(
        "create",
        help="create a game"
    )
    parser_game_create.add_argument("name", type=str, help="Name of the game to create")
    parser_game_create.set_defaults(func=create_game)

    parser_game_delete = subparser.add_parser(
        "delete",
        help="delete a game"
    )
    parser_game_delete.add_argument("id", type=int, help="Id of the game to create")
    parser_game_delete.set_defaults(func=delete_game)


def get_game():
    games = game_manager.get_all()
    return games


def create_game(name):
    game = game_manager.create(name)
    return game


def delete_game(id):
    game_manager.delete(id)
    return "Game deleted"
