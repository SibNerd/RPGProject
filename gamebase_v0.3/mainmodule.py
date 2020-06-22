"""
MAIN GAME MODULE.
ALL THE GAME PROCESSES ARE PLACED HERE.
ALL THE FUNCTIONS CHECKIGS ARE PLASED HERE TOO (FOR NOW).
"""

import menu
import texts

def Main():
    player_fraction = ''
    player_team = []
    print(texts.GREETING_TEXT)
    menu.MainMenu(player_fraction, player_team)

Main()
