
"""
User Story 1.4: Ich möchte Hotels sehen, die während meines Aufenthalts verfügbar sind (Check-in- und Check-out-Datum).
"""


from business_logic.hotel_service import find_hotels_by_availability

DB_PATH = "database/hotel_reservation_sample.db"

def main():
    print("Hotel Search by your availability")
    try:
        check_in_date = input("Enter your check-in Date in the Format: YYYY-MM-DD: ")
        check_out_date = input("Enter your check-out Date in the Format: YYYY-MM-DD: ")
    except ValueError:
        print("Please enter a valid date in the format: YYYY-MM-DD")
        return

    hotels = find_hotels_by_availability(check_in_date, check_out_date)

    if hotels:
        print(f"\nThese hotels are available from {check_in_date} to {check_out_date}:\n")
        for index, (hotel_id, name, stars, city, street) in enumerate(hotels, start=1):
            print(f"{index}. {name} ({stars}★), {street}, {city}")
    else:
        print(f"\nNo hotels vailable from {check_in_date} to {check_out_date}:\n")


