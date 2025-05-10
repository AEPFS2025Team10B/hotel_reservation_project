
"""
User Story 1.5: Ich möchte Wünsche kombinieren können (z.B. Gästezahl, Sterne, Verfügbarkeit).).
"""


from business_logic.hotel_manager import find_hotels_by_multiple_criteria

DB_PATH = "database/hotel_reservation_sample.db"

def main():
    print("Hotel Search by your availability")
    try:
        city = input("Enter a city: ").strip()
        min_stars = int(input("Enter minimum stars: "))
        guest_count = int(input("And how many people should have space in this room? "))
        check_in_date = input("Enter your check-in Date in the Format: YYYY-MM-DD: ")
        check_out_date = input("Enter your check-out Date in the Format: YYYY-MM-DD: ")
    except ValueError:
        print("Please enter a valid date in the format: YYYY-MM-DD")
        return

    hotels = find_hotels_by_multiple_criteria(city, min_stars, guest_count, check_in_date, check_out_date)

    if hotels:
        print(f"\nThese hotels are available for you:\n")
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.street}, {hotel.city}")
    else:
        print(f"\nNo hotels available:\n")


