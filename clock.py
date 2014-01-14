import globals
import colors
import pygame


class Clock:

    def __init__(self, pos):
        self.time = 0
        self.pos = pos
        self.running = True

    def show_clock(self):
        ikona_zegara = pygame.image.load('ikonki/zegarek.png')
        clock_font = pygame.font.Font(globals.counter_and_clock_font, 27)
        text = clock_font.render(
            str(self.time).zfill(2), 1, colors.napisyColor)
        globals.background.blit(ikona_zegara, self.pos)
        pos2 = pygame.Rect(self.pos)
        pos2.x += 25
        pos2.y -= 2
        # shadow
        clock_shadow = clock_font.render(
            str(self.time).zfill(2), 1, colors.shadowColor)
        shadow_pos = pygame.Rect(pos2)
        shadow_pos.x += 2
        shadow_pos.y += 2

        globals.background.blit(clock_shadow, shadow_pos)
        globals.background.blit(text, pos2)

    def update(self):
        # jesli gra sie zakonczyla, zatrzymaj zegar
        if not self.running:
            return
        self.time += 1
        self.clear_clock()
        self.show_clock()

    def clear_clock(self):
        tmp = pygame.Surface((3 * 36 + 2, 30))
        tmp.fill(colors.backgroundColor)
        globals.background.blit(tmp, self.pos)

    def start_clock(self):
        pygame.time.set_timer(globals.UPDATECLOCKEVENT, 1000)
        self.running = True

    def stop_clock(self):
        self.running = False


def main():
    pass

if __name__ == "__main__":
    main()
