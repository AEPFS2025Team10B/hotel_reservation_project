import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ziel ist es dass ein Admin User nach diversen sachen suchen kann, Nationalität, altersspannen,
# oder ob gäste wieder kommen
from business_logic import guest_manager
import pandas as pd


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

    #print_age_groups, print_nationalities & print_recurring_guests separat gemacht,
    # dass es später, falls es anpassungen gibt, einfacher ist


def compute_demographics():
    # Holt sämtliche Demografie-Daten direkt aus der Business-Logik
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
    df_rec = pd.DataFrame(
        [{'Recurring Guests': demographics['recurring_guests']}]
    )

    # .outputs Ordner erstellen, falls nicht vorhanden
    output_dir = '.outputs'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    # Excel-Writer mit XlsxWriter
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        wb  = writer.book

        # Altersgruppen
        df_age.to_excel(writer, sheet_name='Age Groups', index=False)
        ws1 = writer.sheets['Age Groups']
        chart1 = wb.add_chart({'type': 'column'})
        chart1.add_series({
            'name':       'Gäste nach Altersgruppe',
            'categories': ['Age Groups', 1, 0, len(df_age), 0],
            'values':     ['Age Groups', 1, 1, len(df_age), 1],
        })
        chart1.set_title({'name': 'Gäste nach Altersgruppe'})
        ws1.insert_chart('D2', chart1)

        # Nationalitäten
        df_nat.to_excel(writer, sheet_name='Nationalities', index=False)
        ws2 = writer.sheets['Nationalities']
        chart2 = wb.add_chart({'type': 'pie'})
        chart2.add_series({
            'name':       'Gäste nach Nationalität',
            'categories': ['Nationalities', 1, 0, len(df_nat), 0],
            'values':     ['Nationalities', 1, 1, len(df_nat), 1],
        })
        chart2.set_title({'name': 'Gäste nach Nationalität'})
        ws2.insert_chart('D2', chart2)

        # Wiederkehrende Gäste
        df_rec.to_excel(writer, sheet_name='Recurring', index=False)
        ws3 = writer.sheets['Recurring']
        ws3.write('A3', 'Dies ist die Anzahl der wiederkehrenden Gäste.')

    print(f"✅ Excel-Bericht gespeichert unter: {file_path}")


def main():
    print("\nGuest demographic report")

    valid = False
    while not valid:
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

        input(f"\nPress enter to finish")
        valid = True


if __name__ == "__main__":
    main()