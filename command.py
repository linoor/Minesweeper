__author__ = 'linoor'


class GameStateChanger(object):
    """The INVOKER class"""

    @classmethod
    def execute(cls, command):
        command.execute()


class Command(object):
    """The command interface"""

    def __init__(self, obj):
        self._obj = obj

    def execute(self):
        raise NotImplementedError


class StartNewGame(Command):
    """The command for starting a new game"""

    def execute(self):
        self._obj.new_game()


class EndGameBoiler(Command):
    """The command for starting a new game"""

    def execute(self):
        self._obj.end_game_boiler()
