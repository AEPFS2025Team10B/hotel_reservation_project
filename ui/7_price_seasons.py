from business_logic import add_new_booking, apply_seasonal_discount
from business_logic.address_manager import add_new_address
from ui import search_hotels_by_city_01_1
from ui import search_hotel_stars_01_2
from ui import search_room_by_guest_count_01_3
from ui import search_hotels_by_availability_01_4
from ui import search_hotels_by_multiple_criteria_01_5
from ui import search_all_hotel_details_01_6
from business_logic.address_manager import find_address_id
from business_logic.guest_manager import find_guest_by_email
from business_logic.room_manager import get_available_rooms_by_hotel_and_dates
from business_logic.hotel_manager import print_all_hotel_details
from business_logic.hotel_manager import create_detailed_hotel_list
from business_logic.hotel_manager import print_detailed_hotel_list

from business_logic.guest_manager import add_new_guest
from common_code.country_list import COUNTRIES

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

def get_valid_nationality():
    """Get a valid nationality from the user."""
    while True:
        code = input("\nPlease enter your nationality (country code, e.g. 'CH' for Switzerland): ").strip().upper()
        if code in COUNTRIES:
            return COUNTRIES[code]['en']  # Return English country name instead of code

        # Only show the list if the input was invalid
        print("\nInvalid country code. Here are all available countries:")
        sorted_countries = sorted(COUNTRIES.items(), key=lambda x: x[1]['en'])
        for code, names in sorted_countries:
            print(f"{code} = {names['en']}")


def main():
    global selected_hotel
    valid = False
    check_in_date = None
    check_out_date = None
    while not valid:
        # hotels = None #TODO: Eventuell ist das die Lösung für: if isinstance(hotels, tuple) and len(hotels) == 3:
        print("1. Would you like to select the hotel of a list ?")
        print("2. Would you like to search a hotel by city ?")
        print("3. Would you like to search a hotel by city and star ?")
        print("4. Would you like to search a hotel by guest count ?")
        print("5. Would you like to search hotels by availability ?")
        print("6. Would you like to search a hotel by multiple criteria ?")
        user_selection = int(input("Which option would you like? Enter the according number: "))
        if user_selection == 1:
            hotels = search_all_hotel_details_01_6.main()
            # Code von search_all_hotel_details_01_6.py wird wiederverwendet
        elif user_selection == 2:
            hotels = search_hotels_by_city_01_1.main()
            # Code von search_hotels_by_city_01_1.py wird wiederverwendet
        elif user_selection == 3:
            hotels = search_hotel_stars_01_2.main()
            # Code von search_hotel_stars_01_2.py wird wiederverwendet
        elif user_selection == 4:
            hotels = search_room_by_guest_count_01_3.main()
            # Code von search_room_by_guest_count_01_3.py wird wiederverwendet
        elif user_selection == 5:
            hotels, check_in_date, check_out_date = search_hotels_by_availability_01_4.main()
            # Code von search_hotels_by_availability_01_4.py wird wiederverwendet
        elif user_selection == 6:
            hotels, check_in_date, check_out_date = search_hotels_by_multiple_criteria_01_5.main()
            # Code von search_hotels_by_multiple_criteria_01_5.py wird wiederverwendet

        if isinstance(hotels, tuple) and len(hotels) == 3:
            # Already unpacked above, no need to unpack again
            pass

        valid = True

        correct = False
        while not correct:
            if hotels:
                print(print_all_hotel_details(hotels))
                # Alle hotels werden ausgegeben
                selection = int(input(
                    "\nEnter the number of the hotel you want to see the available rooms for your desired stay dates: ").strip())
                if 1 <= selection <= len(hotels):
                    selected = hotels[selection - 1]
                    # Die eingabe vom Kunden wird auf ihre Gültigkeit geprüft
                    selected_hotel_list = create_detailed_hotel_list(selected)
                    selected_hotel = selected_hotel_list[0]
                    print("\nYou selected:")
                    print(print_detailed_hotel_list(selected_hotel))
                    #die Wahl wird nochmal bestätigt
                coach = False
                while not coach:
                    choice = input(f"\nfor coach: Do you want to check when no hotels are available (y/n)?")
                    if choice.lower() == "y":
                        print("enter as check-in: 2025-10-28 an check-out: 2025-10-31")
                        print("")
                        coach = True
                    elif choice.lower() == "n":
                        coach = True
                    else:
                        print("Please enter either 'y' or 'n'.")
                        # das ganze loop ist dafür da um dem coach zu helfen, den Code auf funktionalität zu prüfen

                print("For coach: There will be an about regarding discount either but to get discount enter a check-in-date in March/April/Mai/September/October/November ")
                if not check_in_date:
                    check_in_date = ask_date("Check-in (YYYY-MM-DD): ")
                if not check_out_date:
                    check_out_date = ask_date("Check-out (YYYY-MM-DD): ")
                    # kommt nur zum Zug, wenn noch keine eingabe getätigt wurde.
                    # Je nach dem, was bei vorhin für eine Auswahl getroffen wurde.
                print(f"\nVerfügbare Zimmer vom {check_in_date} bis {check_out_date} in diesem Hotel:")
                rooms = get_available_rooms_by_hotel_and_dates(selected_hotel.hotel_id, check_in_date, check_out_date)
                correct = True
            if rooms:
                rooms, original_prices = apply_seasonal_discount(rooms, check_in_date)
                correct = True
                live = False
                while not live:
                    #Output wird festgelegt:
                    output = ""
                    for index in range(len(rooms)):
                        r = rooms[index]
                        original_price = original_prices[index]
                        output += f"{index + 1} - Room {r.number}: {r.price_per_night} CHF, Type: {r.roomtype.description}, Max Guests: {r.roomtype.max_guests}\n"
                        if original_price != r.price_per_night:
                            output += f"✅ Original: {original_price:.2f} CHF ➜ Discounted: {r.price_per_night:.2f} CHF\n"
                        if r.facilities:
                            for facility in r.facilities:
                                output += f"  - Facility: {facility.name}\n"
                    print(output)
                    #der Output wird ausgegeben

                    room_booking = int(input("\nEnter the number of the room you want to book: ").strip())
                    if 1 <= room_booking <= len(rooms):
                        selected_room = rooms[room_booking - 1]
                        #der Input wird geprüft, muss 1 oder grösser sein, bis anzahl Räme
                    live = True

                    print(f"\nYou have selected  Room number:{selected_room.number}, Price per night: {selected_room.price_per_night}")
                    email = input("\nPlease Enter your email: ")
                    existing_guest = find_guest_by_email(email)
                    if existing_guest:
                        print(
                            f"✅ Existing guest found: {existing_guest.first_name} {existing_guest.last_name} \n You don't have to enter all details again :) ")
                        new_guest = existing_guest

                    else:
                        street = input("\nPlease Enter your street address including house number: ")
                        city = input("\nPlease Enter your city: ")
                        zip = input("\nPlease Enter your zip code: ")
                        birthday = input("\nPlease Enter your birthday (YYYY-MM-DD): ")
                        nationality = get_valid_nationality()
                        first_name = input("\nPlease Enter your first name: ")
                        last_name = input("\nPlease Enter your last name: ")
                        #angeben vom Kunden werden abgefragt

                        address_id = find_address_id(street, city, zip)
                        if not address_id:
                            new_address = add_new_address(street, city, zip)
                            address_id = new_address.address_id
                        new_guest = add_new_guest(first_name, last_name, email, street, city, zip, nationality,
                                                  birthday)

                    new_booking = add_new_booking(email, selected_room, check_in_date, check_out_date,
                                                  selected_hotel)
                    print(new_booking)
                    try:
                        input("\nPress Enter to finish")
                        return
                    except (EOFError, KeyboardInterrupt):
                        print("\nBooking completed successfully!")
                        #dem Kunden wird bestätigt, das die Buchung funktioniert hat.
                        return

            if not rooms:
                print("No available rooms, in all the hotels in this time period.")
                #dem Kunden wird mitgeteilt, dass es zum gewünschten Zeitpunkt keine verfügbaren Hotels hat
                input("\nPress Enter to finish")
                live = True

        else:
            print("Invalid selection. Please try again.")
    else:
        print("No hotels available for the selected criteria. Please try different dates or criteria.")
        # dem Kunden wird mitgeteilt, dass es mit den gewünschten Kriterien keine verfügbaren Hotels hat
        return


