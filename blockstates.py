import os
import pygame
from globals import ikonki_directory

__author__ = 'linoor'


class BlockState(object):
    def update(self):
        self.block.image = pygame.image.load(os.path.join(ikonki_directory, self.ikonka))
        return self


class FlaggedState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'flag.png'

    def update(self):
        super(FlaggedState, self).update()
        self.block.flagged = True
        return self

    def right_click(self, counter):
        self.block.state = self.block.question_state.update()
        counter.mines += 1
        counter.update()


class CoveredState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'aktywne.png'

    def update(self):
        super(CoveredState, self).update()
        self.block.flagged = False
        self.block.question = False
        return self

    def right_click(self, counter):
        self.block.state = self.block.flagged_state.update()
        counter.mines -= 1
        counter.update()


class QuestionState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'mark.png'

    def update(self):
        super(QuestionState, self).update()
        self.block.flagged = False
        self.block.question = True
        return self

    def right_click(self, counter):
        self.block.state = self.block.covered_state.update()


class MinedState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'mina.png'

    def update(self):
        super(MinedState, self).update()
        self.block.covered = False
        return self

    def right_click(self):
        pass


class ExplodedState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'exploded.png'

    def update(self):
        super(ExplodedState, self).update()
        self.block.covered = False
        return self

    def right_click(self):
        pass


class NotMinedUncoveredState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'nieaktywne.png'

    def update(self):
        mines_surrounding = self.block.mines_surrounding
        if mines_surrounding != 0:
            self.ikonka = '%d.png' % mines_surrounding
        super(NotMinedUncoveredState, self).update()
        self.block.covered = False
        return self

    def right_click(self):
        pass