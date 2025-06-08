from business_logic.room_manager import get_available_rooms_by_hotel
from datetime import date, timedelta

def get_next_available_date_for_hotel(
        hotel_id: int,
        room_type_id: int = None,
        start_date: date = None,
        lookahead_days: int = 365
    ) -> date | None:
    """
    Findet das nächste Datum innerhalb von `lookahead_days`, an dem mindestens ein Zimmer im Hotel verfügbar ist.

    :param hotel_id: ID des Hotels
    :param room_type_id: (Optional) ID des Raumtyps, wenn nur bestimmte Zimmertypen geprüft werden sollen
    :param start_date: (Optional) Startdatum für die Suche; Standard ist heute
    :param lookahead_days: Anzahl Tage, wie weit im Voraus gesucht wird
    :return: Datum des nächsten freien Tages oder None, wenn innerhalb des Zeitraums kein freier Tag gefunden wurde
    """
    if start_date is None:
        current = date.today()
    else:
        current = start_date

    for offset in range(lookahead_days + 1):
        check_date = current + timedelta(days=offset)
        try:
            # Versuche mit Room-Type
            available = get_available_rooms_by_hotel(hotel_id, check_date, room_type_id)
        except TypeError:
            # Fallback, falls kein room_type_id akzeptiert wird
            available = get_available_rooms_by_hotel(hotel_id, check_date)
        if available:
            return check_date

    return None