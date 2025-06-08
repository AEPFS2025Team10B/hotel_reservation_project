# find_hotels_by_list_city haben wir implementiert, da wir nicht wollten,
# dass sich unser code bei der user story 1.1 & 1.2 wiederholt.
# Bei uns haben nämlich beide zu einem grossem teil dasselbe UI.

def find_hotel_by_list_city(hotels):
    if len(hotels) > 1:
        print("\nAvailable hotels:")
        for i, hotel in enumerate(hotels, start=1):
            print(f"{i}. {hotel.name} ({hotel.stars}★), Address: {hotel.address.street}, {hotel.address.zip_code}, {hotel.address.city}")

    while True:
        try:
            selection = int(input("\nEnter the number of the hotel you'd like to view in more detail: "))
            if 1 <= selection <= len(hotels):
                selected = hotels[selection - 1]
                print("\nYou selected:")
                print(f"→ {selected.name}")
                print(f"  {selected.stars}★, {selected.address}")
                input("\nPress Enter to finish...")
                return selected
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
