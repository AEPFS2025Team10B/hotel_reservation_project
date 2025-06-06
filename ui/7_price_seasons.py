from business_logic import add_new_booking, apply_seasonal_discount
from business_logic.address_manager import add_new_address
from model import hotel
from ui import search_hotels_by_city_01_1
from ui import search_hotel_stars_01_2
from ui import search_room_by_guest_count_01_3
from ui import search_hotels_by_availability_01_4
from ui import search_hotels_by_multiple_criteria_01_5
from ui import search_all_hotel_details_01_6
from model import guest
from business_logic.guest_manager import add_new_guest
from business_logic.room_manager import get_available_rooms_by_hotel_and_dates_2
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def ask_date(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        try:
            datetime.strptime(s, DATE_FORMAT)
            return s
        except ValueError:
            print("Please enter a date in the format: YYYY-MM-DD.")


def main ():
    valid = False
    check_in_date = None
    check_out_date = None
    while not valid:
        #hotels = None #TODO: Eventuell ist das die Lösung für: if isinstance(hotels, tuple) and len(hotels) == 3:
        print("1. Would you like to select the hotel of a list ?")
        print("2. Would you like to search a hotel by city ?")
        print("3. Would you like to search a hotel by city and star ?")
        print("4. Would you like to search a hotel by guest count ?")
        print("5. Would you like to search hotels by availability ?")
        print("6. Would you like to search a hotel by multiple criteria ?")
        user_selection = int(input("Which option would you like? Enter the according number: "))
        if user_selection == 1:
            hotels = search_all_hotel_details_01_6.main()
        elif user_selection == 2:
            hotels = search_hotels_by_city_01_1.main()
        elif user_selection == 3:
            hotels = search_hotel_stars_01_2.main()
        elif user_selection == 4:
            hotels = search_room_by_guest_count_01_3.main()
        elif user_selection == 5:
            hotels, check_in_date, check_out_date = search_hotels_by_availability_01_4.main()
        elif user_selection == 6:
            hotels, check_in_date, check_out_date = search_hotels_by_multiple_criteria_01_5.main()

        if isinstance(hotels, tuple) and len(hotels) == 3:
            hotels, check_in_date, check_out_date = hotels

        valid = True
    correct = False
    while not correct:
        if hotels:
            for index, hotel in enumerate(hotels, start=1):
                print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.address}")
        selection = int(input("\nEnter the number of the hotel you want to see the available rooms for your desired stay dates: ").strip())
        if 1 <= selection <= len(hotels):
            selected_hotel = hotels[selection - 1]
        if not check_in_date:
            check_in_date = ask_date("Check-in (YYYY-MM-DD): ")
        if not check_out_date:
            check_out_date = ask_date("Check-out (YYYY-MM-DD): ")
        correct = True
        print(f"\nVerfügbare Zimmer vom {check_in_date} bis {check_out_date} in diesem Hotel:")
        rooms = get_available_rooms_by_hotel_and_dates_2(selected_hotel.hotel_id, check_in_date, check_out_date)
        rooms = apply_seasonal_discount(rooms, check_in_date)
        live = False
        while not live:
            if rooms:
                for index, r in enumerate(rooms, start=1):
                    print(f"{index} - room {r.number}, Room Type {r.roomtype} CHF {r.price_per_night:.2f} per night")
                room_booking = int(input("\nEnter the number of the room you want to book: ").strip())
                if 1 <= selection <= len(rooms):
                    selected_room = rooms[room_booking - 1]
                live = True
                print(f"\nYou have selected  {selected_room}")
                street = input("\nPlease Enter your street address including house number: ")
                city = input("\nPlease Enter your city: ")
                zip = input("\nPlease Enter your zip code: ")
                first_name = input("\nPlease Enter your first name: ")
                last_name = input("\nPlease Enter your last name: ")
                email = input("\nPlease Enter your email: ")
                new_address = add_new_address(street, city, zip)
                new_guest = add_new_guest(first_name, last_name, email, street, city, zip)
                new_booking = add_new_booking(email, selected_room, check_in_date, check_out_date)
                return

            if not rooms:
                print("No available rooms, in all the hotels in this time period.")




