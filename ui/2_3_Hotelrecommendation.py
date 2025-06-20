"""
3. Als Gast möchte ich nach meinem Aufenthalt Hotelbewertungen abgeben
"""
#Ziel ist es, dass der User die Buchungs ID eingeben muss, diese dann zuerst abgeglichen wir,
# ob sie überhaupt existiert.
# Danach kann der User seine Bewertung abgeben und es wird gespeichert.


from business_logic.booking_manager import find_booking_by_id, add_new_hotelrecommendation


#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def main():
    print("\n=== Hotel Recommendation System ===")
    print("Please provide your feedback for your stay.")
    ask_booking_id()

def ask_booking_id():
    valid = False
    while not valid:
        print(f"\nfor Coach: You can use booking id: 1\n")
        user_input = int(input("Please enter your booking id: "))
        booking = find_booking_by_id(user_input)
        #Das Loop wird noch im Manager geschlossen
        
        if booking is None:
            print("No booking found with this ID. Please try again.")
            #Kunde wird informiert, dass er keine gültige Buchungs-Id eingegeben hat.

            continue
            #loop wird fortgesetzt
            
        print("\nBooking Details:")
        print(f"Booking ID: {booking.booking_id}")
        print(f"Check-in Date: {booking.check_in_date}")
        print(f"Check-out Date: {booking.check_out_date}")
        print(f"Room: {booking.room.number}")
        print(f"Guest: {booking.guest.first_name} {booking.guest.last_name}")
        print(f"Total Amount: {booking.total_price}")
        #Die details werden für den Kunden nochmals ausgegeben, dass er auch sicher ist,
        # dass auch wirklich die Hotelbewertung richtig hinterlegt wird.

        #TODO: wenn genug zeit, die angaben nicht printen,
        # sondern den Kunden dazu bringen Booking ID und seinen Namen und/oder E-Mail einzugeben

        correct = input("Is this your booking? (Y/N): ")
        if correct.lower() == "y":
            ask_hotelrecommendation(booking)
            return
        elif correct.lower() == "n":
            print("Alright, the process has been canceled.")
            # Kunde kann hier bestätigen, ob es sich um seine Buchung handelt oder nicht,
            # wenn nicht, wird das Programm beendet
            input(f"\nPress Enter to Exit")
            #TODO: Quit ersetzen, mit einem auswahlmenü, möchten Sie Ihre Buchung erneut suchen
            quit()


# Wir haben uns dazu entschieden zwei funktionen zu machen.
# Idee: Falls mal ein Problem auftreten sollte, ist es für uns einfach den Code wieder zu verstehen
def ask_hotelrecommendation(booking):
    rating = None
    recommendation = None
    valid = False
    while not valid:
        try:
            rating = int(input("\nPlease enter your rating (1-10): "))
            if 1 <= rating <= 10:
                #es wird geprüft, ob das eingegebene Rating unsren Vorgaben entspricht (muss zwischen 1 und 10 sein)
                valid = True
            else:
                print("Invalid input please enter 1 to 10.")
                #Kunde wird informiert, dass er ein ungültiges Rating eingegeben hat.

        except ValueError:
            print("Invalid input please enter 1 to 10.")
            # Kunde wird informiert, dass er ein ungültiges Rating eingegeben hat.

    valid = False
    while not valid:
    #schleife, weil der Kunde bei einem fehler (zu viele Zeichen) nicht alles von vorne beginnen möchte.
        try:
            recommendation = input("\nPlease enter your recommendation(not mandatory): ")
            if recommendation == "" or len(recommendation) <= 500:
                #Begrenzt Anzahl Zeichen auf max. 500
                valid = True
            else:
                print("The recommendation can not be longer than 500 characters")
                #Kunde wird informiert, dass seine Bewertung zu lange war

        except Exception as e:
            print(f"Unexpected error: {e}")
    
    try:
        if recommendation is None:
            recommendation = ""
        add_new_hotelrecommendation(booking.booking_id, rating, recommendation)
        #Inputs werden an Booking Manager zurückgegeben
        print(f"\nThank you for your feedback!\n")
        input("Press Enter to Exit")
    except ValueError as e:
        print(f"Error saving your feedback: {e}")


#Aktuell wird rating und recommendation immer überschrieben. So wie es bis jetzt aufgebaut ist,
# noch nicht 100% sinn. Der Kunde muss nur mit Y/N bestätigen, dass es sich um seine Buchung handelt.
# Jemand anderes könnte also alles überschreiben, weil es aber noch nicht besser geschützt ist, macht
# es aber auch sinn, dass das rating immer überschrieben wird. Wir würden also noch implementieren,
# dass der Kunde zusätzlich noch seinen Namen angeben muss oder wir würden in der Datenbank eine neue
# Tabelle erstelle "Hotelrecommendation", dann könnte, dann wäre es unabhängig von der Buchung und
# jeder kann eine Bewertung abgeben, auch wenn man selbst nicht der ist, der auf der Buchung hinterlegt ist.

if __name__ == "__main__":
    #print(os.getcwd())
    #ask_booking_id()
    main()