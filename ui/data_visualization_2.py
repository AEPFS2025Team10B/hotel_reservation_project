import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic import guest_manager

def print_age_groups(demographics):
    print("\nAge groups:")
    if demographics["age_groups"]:
        for age_range, count in sorted(demographics["age_groups"].items()):
            print(f"  {age_range}: {count} Gäste")
    else:
        print("No age data available.")

def print_nationalities(demographics):
    print("\nNationalities:")
    if demographics["nationalities"]:
        for nationality, count in sorted(demographics["nationalities"].items()):
            print(f"  {nationality}: {count} Gäste")
    else:
        print("No nationality data available.")

def print_recurring_guests(demographics):
    print("\nRecurring guests:")
    print(f"Amount recurring guests: {demographics["recurring_guests"]} ")

def main():
    print("\nGuest demographic report")

    demographics = guest_manager.get_guest_demographics()
    valid = False
    while not valid:
        print("\nWas möchten Sie sehen?")
        print("1. Age groups")
        print("2. Nationalities")
        print("3. Recurring guests")
        print("4. show all data")
        print("5. to finish the program")

        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid. please enter a number.")
            continue

        if choice == 1:
            print_age_groups(demographics)
            print("")
            input("Press enter to finish")
            valid = True
        elif choice == 2:
            print_nationalities(demographics)
            print("")
            input("Press enter to finish")
            valid = True
        elif choice == 3:
            print_recurring_guests(demographics)
            print("")
            input("Press enter to finish")
            valid = True
        elif choice == 4:
            print_age_groups(demographics)
            print_nationalities(demographics)
            print_recurring_guests(demographics)
            print("")
            input("Press enter to finish")
            valid = True

        elif choice == 0:
            break
        else:
            print("invalid choice. Please try again.")

if __name__ == "__main__":
    main()
