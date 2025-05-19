"""
User Story 3.3: Ich möchte Hotel Infos updaten
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import update_hotel

def main():
    print("__________________________")
    print("|- Update Hotel Details -|")
    print("__________________________")
    hotels = update_hotel()

    if not hotels:
