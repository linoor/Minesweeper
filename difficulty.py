# -*- coding: utf-8 -*-
""" klasa odzwierciedlająca poziom trudności. Zawiera takie dane jak: wielkość planszy, ilość min na planszy, wielkość pola """


class Difficulty:

    def __init__(self, width, height, mines_number, field_size, name):
        self.name = name
        self.mines_number = mines_number
        self.height = height * field_size + (height + 1)
        self.width = width * field_size + (width + 1)


def main():
    pass

if __name__ == "__main__":
    main()
