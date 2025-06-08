import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ziel ist es dass ein Admin User nach diversen Sachen suchen kann: Nationalität, Altersspannen, oder ob Gäste wiederkommen
from business_logic import guest_manager
from data_access import GuestDataAccess, BookingDataAccess
import pandas as pd
from datetime import date


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
    print(f"Amount recurring guests: {demographics['recurring_guests']} ")

    # print_age_groups, print_nationalities & print_recurring_guests separat gemacht,
    # damit spätere Anpassungen einfacher sind


def compute_demographics():
    # Holt aggregierte Demografie-Daten aus der Business-Logik
    return guest_manager.get_guest_demographics()


def export_demographics_to_excel(filename="guest_demographics_report.xlsx"):
    # Alle Daten auswerten
    demographics = compute_demographics()

    # DataFrames erstellen
    df_age = pd.DataFrame(
        list(demographics['age_groups'].items()),
        columns=['Age Group', 'Count']
    )
    df_nat = pd.DataFrame(
        list(demographics['nationalities'].items()),
        columns=['Nationality', 'Count']
    )

    # DataFrame für wiederkehrende Gäste mit Details
    guest_dao = GuestDataAccess()
    booking_dao = BookingDataAccess()
    all_guests = guest_dao.get_all_guests()
    all_bookings = booking_dao.get_all_bookings()

    # Statistiken pro Gast sammeln
    stats = {}
    for b in all_bookings:
        gid = b.guest_id
        ci = b.check_in_date
        co = b.check_out_date
        nights = (co - ci).days if isinstance(co, date) and isinstance(ci, date) else 0
        if gid not in stats:
            stats[gid] = {'visits': 0, 'nights': 0, 'last_stay': None}
        stats[gid]['visits'] += 1
        stats[gid]['nights'] += nights
        if stats[gid]['last_stay'] is None or co > stats[gid]['last_stay']:
            stats[gid]['last_stay'] = co

    rows = []
    for gid, data in stats.items():
        if data['visits'] > 1:
            guest = next((g for g in all_guests if g.guest_id == gid), None)
            name = f"{guest.first_name} {guest.last_name}" if guest else str(gid)
            rows.append({
                'Guest Name': name,
                'Visits': data['visits'],
                'Total Nights': data['nights'],
                'Last Stay': data['last_stay']
            })
    df_rec = pd.DataFrame(rows)

    # .outputs Ordner erstellen, falls nicht vorhanden
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    # Excel-Writer mit XlsxWriter
    with pd.ExcelWriter(file_path, engine='xlsxwriter', datetime_format='yyyy-mm-dd') as writer:
        wb = writer.book

        # Altersgruppen
        df_age.to_excel(writer, sheet_name='Age Groups', index=False)
        ws1 = writer.sheets['Age Groups']
        chart1 = wb.add_chart({'type': 'column'})
        chart1.add_series({
            'name': 'Gäste nach Altersgruppe',
            'categories': ['Age Groups', 1, 0, len(df_age), 0],
            'values': ['Age Groups', 1, 1, len(df_age), 1],
        })
        chart1.set_title({'name': 'Gäste nach Altersgruppe'})
        ws1.insert_chart('D2', chart1)

        # Nationalitäten
        df_nat.to_excel(writer, sheet_name='Nationalities', index=False)
        ws2 = writer.sheets['Nationalities']
        chart2 = wb.add_chart({'type': 'pie'})
        chart2.add_series({
            'name': 'Gäste nach Nationalität',
            'categories': ['Nationalities', 1, 0, len(df_nat), 0],
            'values': ['Nationalities', 1, 1, len(df_nat), 1],
        })
        chart2.set_title({'name': 'Gäste nach Nationalität'})
        ws2.insert_chart('D2', chart2)

        # Wiederkehrende Gäste mit Details
        df_rec.to_excel(writer, sheet_name='Recurring', index=False)
        ws3 = writer.sheets['Recurring']
        ws3.write('A1', 'Gastname, Anzahl Besuche, Gesamtanzahl Nächte, Letzter Aufenthalt')

    print(f"✅ Excel-Bericht gespeichert unter: {file_path}")


def main():
    print("\nGuest demographic report")

    while True:
        print("\nWas möchten Sie sehen?")
        print("1. Age groups")
        print("2. Nationalities")
        print("3. Recurring guests")
        print("4. show all data")
        print("5. Export to Excel")
        print("0. to finish the program")

        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid. please enter a number.")
            continue

        demographics = compute_demographics()
        if choice == 1:
            print_age_groups(demographics)
        elif choice == 2:
            print_nationalities(demographics)
        elif choice == 3:
            print_recurring_guests(demographics)
        elif choice == 4:
            print_age_groups(demographics)
            print_nationalities(demographics)
            print_recurring_guests(demographics)
        elif choice == 5:
            export_demographics_to_excel()
        elif choice == 0:
            break
        else:
            print("invalid choice. Please try again.")
            continue

        print("")
        input("Press enter to finish")


if __name__ == "__main__":
    main()