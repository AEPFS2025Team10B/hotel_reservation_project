"""
User Story 1.1
As a user, I want to search for hotels in a specific city so that I can find suitable accommodations.
"""

from business_logic.hotel_service import find_hotels_by_city

def main():
    print("🏨 Hotel Search by City")
    city = input("Enter a city: ").strip()
    hotels = find_hotels_by_city(city)

    if hotels:
        print(f"\nFound hotels in {city}:")
        for name, stars, city, street in hotels:
            print(f"- {name} ({stars}★), {street}, {city}")
    else:
        print(f"\nNo hotels found in {city}.")

if __name__ == "__main__":
    main()