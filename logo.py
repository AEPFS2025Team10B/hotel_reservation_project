import os

# ANSI color codes for terminal
_YELLOW = '\033[93m'
_CYAN = '\033[96m'
_MAGENTA = '\033[95m'
_RESET = '\033[0m'

def print_logo():
    # Clear the terminal for a fresh look
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # ASCII art header
    header = r"""
  ____  _           _   _       _   _                 
 |  _ \| |__   __ _| |_| |__   | |_| |__   ___  _ __  
 | |_) | '_ \ / _` | __| '_ \  | __| '_ \ / _ \| '_ \ 
 |  __/| | | | (_| | |_| | | | | |_| | | | (_) | | | |
 |_|   |_| |_|\__,_|\__|_| |_|  \__|_| |_|\___/|_| |_|
    """
    print(_CYAN + header + _RESET)
    
    # Subtitle and team info
    print(_YELLOW + "        FS25 Anwendungsentwicklung mit Python".center(60) + _RESET)
    print(_YELLOW + "                   B-TEAM-10".center(60) + _RESET)
    print(_MAGENTA + "-" * 60 + _RESET)
    print(_MAGENTA + " Teammembers: David Germann | Jeremy Nathan | Reto Lutz ".center(60) + _RESET)
    print()
