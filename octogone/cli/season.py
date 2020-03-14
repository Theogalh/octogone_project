from pprint import pprint
from octogone.managers.season import SeasonManager

season_manager = SeasonManager()


def subparser_install(subparser):
    parser_season_get_all = subparser.add_parser(
        "get_all",
        help='get all season'
    )
    parser_season_get_all.set_defaults(func=get_season)

    parser_season_create = subparser.add_parser(
        "create",
        help="create a season"
    )
    parser_season_create.add_argument("name", type=str, help="Name of the season to create")
    parser_season_create.set_defaults(func=create_season)


def get_season():
    seasons = season_manager.get_all()
    return seasons


def create_season(name):
    season = season_manager.create(name)
    return season

