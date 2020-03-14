#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from octogone.app import application, db
from octogone.cli.game import subparser_install as game_subparser
from octogone.cli.game_rule import subparser_install as game_rule_subparser
from octogone.cli.season import subparser_install as season_subparser
# from octogone.cli.right import subparser_install as right_subparser

MAIN_COMMANDS = [
    ('game', game_subparser),
    ('game_rule', game_rule_subparser),
    ('season', season_subparser),
    # ('right', right_subparser),
]


def main():
    """
    Main entry point
    """
    parser = ArgumentParser()

    subparser = parser.add_subparsers(dest='main_command', help='The main command')
    subparser.required = True

    for command in MAIN_COMMANDS:
        cmd_parser = subparser.add_parser(command[0])
        cmd_subparser = cmd_parser.add_subparsers(dest='sub_command', help='The {0} sub-command'.format(command[0]))
        cmd_subparser.required = True
        command[1](cmd_subparser)

    argument = parser.parse_args()
    function = argument.func
    delattr(argument, 'func')
    delattr(argument, 'sub_command')
    delattr(argument, 'main_command')
    with application.app_context():
        message = function(**vars(argument))
        db.session.commit()
        print(message)


if __name__ == "__main__":
    main()
