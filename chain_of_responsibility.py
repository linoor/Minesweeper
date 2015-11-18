__author__ = 'linoor'


class Checker(object):
    def __init__(self, successor=None):
        self._successor = successor

    def check(self, request):
        res, end = self._check(request)
        if not end:
            self._successor.handle(request)
        else:
            return res

    def _check(self, request):
        raise NotImplementedError('Must provide implementation in subclass.')
