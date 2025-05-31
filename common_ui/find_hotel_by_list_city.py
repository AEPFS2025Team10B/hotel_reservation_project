def find_hotel_by_list_city(hotels):
    if len(hotels) > 1:
        print("\nAvailable hotels:")
        for i, hotel in enumerate(hotels, start=1):
            print(f"{i}. {hotel.name} ({hotel.stars}★), {hotel.address}")

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
