import os

# ANSI color codes für Terminal
_YELLOW  = '\033[93m'
_CYAN    = '\033[96m'
_MAGENTA = '\033[95m'
_BLINK   = '\033[5m'
_RESET   = '\033[0m'

def print_logo():
    # Bildschirm löschen
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII-Art Header
    header = r"""
  ____  _           _   _       _   _                 
 |  _ \| |__   __ _| |_| |__   | |_| |__   ___  _ __  
 | |_) | '_ \ / _` | __| '_ \  | __| '_ \ / _ \| '_ \ 
 |  __/| | | | (_| | |_| | | | | |_| | | | (_) | | | |
 |_|   |_| |_|\__,_|\__|_| |_|  \__|_| |_|\___/|_| |_|
    """
    print(_CYAN + header + _RESET)

    # Subtitle und Team-Info
    print(_YELLOW + "        FS25 Anwendungsentwicklung mit Python".center(60) + _RESET)
    print(_YELLOW + "                   B-TEAM-10".center(60) + _RESET)
    print(_MAGENTA + "-" * 60 + _RESET)
    print(_MAGENTA + " Teammembers: David Germann | Jeremy Nathan | Reto Lutz ".center(60) + _RESET)
    print()

    # Blinkender Start­prompt
    prompt = _BLINK + "Enter Y to start".center(60) + _RESET
    choice = input(prompt + "\n").strip().lower()
    while choice != 'y':
        choice = input("Pleas enter Y to start: ").strip().lower()

    # Sobald Y gedrückt wurde, kehrt die Funktion zurück und
    # der restliche Programm-Flow (User-Story-Auswahl) läuft weiter.