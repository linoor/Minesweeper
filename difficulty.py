#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

# -*- coding: utf-8 -*-
""" klasa odzwierciedlająca poziom trudności. Zawiera takie dane jak: wielkość planszy, ilość min na planszy, wielkość pola """
from optparse import OptionParser


class Difficulty:

    def __init__(self, width, height, mines_number, field_size, name):
        self.name = name
        self.mines_number = mines_number
        self.height = height * field_size + (height + 1)
        self.width = width * field_size + (width + 1)


def main():
    pass

def help_text():
    help_message = """
Jest to klasa, któraj jest odpowiedzialna za przechowywanie dostępnych poziomów trudności.

Autor: Michał Pomarański

Aby rozpocząć nową grę należy wcisnąć klawisz 'n' na klawiaturze lub kliknąć na napis 'SAPER'.

Saper korzysta z Pythona 2.7 oraz PyGame 1.9.1 dla Pythona 2.7

Aby zainstalować pygame pod Linuksem:
sudo apt-get install python-pygame

Aby uruchomić grę:
python main.py
"""
    print(help_message)

if __name__ == '__main__':
    parser = OptionParser()
    parser.print_help = help_text
    (options, args) = parser.parse_args()

