"""
4. Als Gast möchte ich Hotelbewertungen vor der Buchung lesen
"""
#Zie ist es, das der Kunde von einer Liste von Hotels eines auswählen kann und
# von diesem dann die Bewertungen siht und lesen kann.


from business_logic.hotel_manager import print_all_hotel_details
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_all_hotel_details
from business_logic.booking_manager import get_reviews_by_hotel_name

def main():
    print("All Hotels")
    hotels = find_all_hotel_details()
    
    if hotels:
        print(print_all_hotel_details(hotels))
        #Alle Hotels werden als Auswahlmenü aufgelistet
        valid = False
        while not valid:
            try:
                coach = False
                while not coach:
                    choice = input(
                        "for coach: do you want to see what happens if a hotel does not have a recommendation (y/n)?")
                    if choice.lower() == "y":
                        print(f"\nChoose the hotel 6. Widder Hotel")
                        coach = True
                    elif choice.lower() == "n":
                        coach = True
                    else:
                        print("Please enter either 'y' or 'n'.")
                        # das ganze loop ist dafür da um dem coach zu helfen, den Code auf funktionalität zu prüfen

                selection = int(input("\nPlease enter the number of the hotel you want to see the recommendations of: ").strip())
                if 1 <= selection <= len(hotels):
                    selected_hotel = hotels[selection - 1]
                    print(f"\nRecommendation(s) for {selected_hotel.name}:")
                    reviews = get_reviews_by_hotel_name(selected_hotel.name)
                    if reviews:
                        # Mittelwert berechnen
                        ratings = [r[0] for r in reviews if r[0] is not None]
                        if ratings:
                            avg_rating = round(sum(ratings) / len(ratings), 1)
                            print(f"Average Rating: {avg_rating}/10\n")
                            #das durchschnittliche rating wird ausgegeben
                        else:
                            print("No recommendation jet, for this hotel.\n")
                            input("Press enter to finish")
                            valid = True
                        # Einzelne Reviews ausgeben
                        for rating, recommendation, first_name, last_name in reviews:
                            rec_text = '' if not recommendation or str(recommendation).lower() == 'none' else recommendation
                            print(f"- {rating}/10 from {first_name} {last_name}: '{rec_text}'")
                            valid = True
                        input(f"\nPress enter to finish")
                    else:
                        print("There are no recommendations for this Hotel.")
                        input(f"\nPress enter to finish")
                        valid = True
                        #TODO: wenn es keine Bewertung gibt, soll nur diese Meldung angezeigt werden
                        #wenn es kein Rating hat, kommt diese Meldung zum Zug,
                        #sieht nicht optimal aus aber ist auch nicht so, dass es nicht funktioniert
                else:
                    print("Invalid Input. Please try again.")
                    #kommt zum zug, wenn man eine nummer eingibt,
                    # die es nicht gibt (bsp. 10 hotels aufgelistet, man gibt 11 ein).

            except ValueError:
                print("Pleas enter a valid number.")
                #es wird ein Integer verlangt, kommt keiner, wird diese Meldung angezeigt
    else:
        print("no hotels found.")
        input(f"\nPress enter to finish")
        #kommt nur zum Zug, wenn es keine Hotels in der Datenbank gibt

if __name__ == "__main__":
    main()
