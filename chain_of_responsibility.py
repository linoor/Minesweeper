__author__ = 'linoor'


class EndGameChecker(object):
    def __init__(self, successor=None):
        self._successor = successor

    def check(self, game):
        print(self.__class__)
        res = self._check(game)
        if res is None:
            return self._successor.check(game)
        else:
            return res

    def _check(self, request):
        raise NotImplementedError('Must provide implementation in subclass.')


class MinefieldSetChecker(EndGameChecker):
    def _check(self, game):
        return False if not game.minefield.are_mines_set else None


class MineHitChecker(EndGameChecker):
    def _check(self, game):
        return True if any(not b.covered and b.mined for b in game.minefield.get_blocks()) else None


class AllFieldsFlaggedChecker(EndGameChecker):
    def _check(self, game):
        return True if all(b.flagged for b in game.minefield.get_blocks() if b.mined) else None


class AllMinesUncovered(EndGameChecker):
    def _check(self, game):
        return True if all(not b.covered for b in game.minefield.get_blocks() if not b.mined) else None


class DefaultChecker(EndGameChecker):
    def _check(self, game):
        return False
