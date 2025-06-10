#!/usr/bin/env python3
"""
add_example_data.py

Befüllt alle Tabellen mit jeweils mindestens fünf Datensätzen.
Löscht vorher vorhandene Daten, um Konflikte zu vermeiden.
"""
import os
import sqlite3

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, '..', 'database', 'hotel_reservation_sample.db')
    print(f"Verbinde mit Datenbank: {db_path}")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    sql = r"""
PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;

-- Vorhandene Daten löschen (Kind- vor Eltern-Tabellen)
DELETE FROM Invoice;
DELETE FROM Booking;
DELETE FROM Room_Facilities;
DELETE FROM Room;
DELETE FROM Facilities;
DELETE FROM Room_Type;
DELETE FROM Guest;
DELETE FROM Hotel;
DELETE FROM Address;

-- Adressen (5 Einträge)
INSERT INTO Address(street, city, zip_code) VALUES
  ('Bahnhofstrasse 1',    'Zürich', '8001'),
  ('Langstrasse 60',      'Zürich', '8004'),
  ('Seefeldstrasse 20',   'Zürich', '8008'),
  ('Marktgasse 59',       'Bern',   '3011'),
  ('Freiestrasse 10',     'Basel',  '4051');

-- Hotels (5 Einträge)
INSERT INTO Hotel(name, stars, address_id) VALUES
  ('Hotel Baur au Lac',              5, 1),
  ('Four Seasons Hôtel des Bergues', 5, 2),
  ('Grand Hotel National',           5, 3),
  ('Bellevue Palace',                5, 4),
  ('Les Trois Rois',                 5, 5);

-- Gäste (5 Einträge)
INSERT INTO Guest(first_name, last_name, email, birthday, nationality, address_id) VALUES
  ('Anna',    'Meier',    'anna.meier@example.com', '1990-01-15', 'Germany', 1),
  ('Benedikt','Frey',     'benedikt.frey@example.com', '1985-06-20', 'United Kingdom', 1),
  ('Claudia', 'Zürcher',  'claudia.zuercher@example.com', '1995-03-10', 'Germany', 2),
  ('Daniel',  'Huber',    'daniel.huber@example.com', '1988-12-05', 'Germany', 3),
  ('Elena',   'Schmid',   'elena.schmid@example.com', '1992-08-25', 'United Kingdom', 4),
  ('Thomas',  'Weber',    'thomas.weber@example.com', '1978-11-30', 'Switzerland', 1),
  ('Maria',   'Koller',   'maria.koller@example.com', '1982-04-15', 'Austria', 2),
  ('Peter',   'Müller',   'peter.mueller@example.com', '1991-07-22', 'Germany', 3);

-- Zimmertypen (5 Einträge)
INSERT INTO Room_Type(description, max_guests) VALUES
  ('Single', 1),
  ('Double', 2),
  ('Suite',  2),
  ('Family', 4),
  ('Deluxe', 2);

-- Einrichtungen (5 Einträge)
INSERT INTO Facilities(facility_name) VALUES
  ('WiFi'),
  ('Frühstück'),
  ('Parkplatz'),
  ('Pool'),
  ('Spa');

-- Zimmer (5 Einträge)
INSERT INTO Room(hotel_id, room_number, type_id, price_per_night) VALUES
  (1, '101', 1, 120.00),
  (2, '102', 2, 180.00),
  (3, '201', 3, 300.00),
  (4, '202', 4, 220.00),
  (5, '203', 5, 250.00);

-- Room_Facilities (5 Einträge)
INSERT INTO Room_Facilities(room_id, facility_id) VALUES
  (1,1),(2,2),(3,3),(4,4),(5,5);

-- Buchungen (5 Einträge, Mai–Aug 2025)
INSERT INTO Booking(guest_id, room_id, check_in_date, check_out_date) VALUES
  (1, 1, '2025-05-20','2025-05-22'),
  (2, 2, '2025-06-01','2025-06-03'),
  (3, 3, '2025-07-10','2025-07-12'),
  (4, 4, '2025-08-05','2025-08-07'),
  (5, 5, '2025-08-20','2025-08-22');

-- Zusätzliche Buchungen für Oktober 2025 (realistische Überlappungen)
INSERT INTO Booking(guest_id, room_id, check_in_date, check_out_date) VALUES
  (1, 1, '2025-10-25','2025-11-02'),  -- Langer Aufenthalt
  (6, 2, '2025-10-26','2025-10-29'),  -- Kurzer Aufenthalt
  (3, 3, '2025-10-27','2025-10-30'),  -- Überlappt mit anderen
  (7, 4, '2025-10-28','2025-10-31'),  -- Hauptzeitraum
  (8, 5, '2025-10-29','2025-11-01'),  -- Versetzt
  (2, 1, '2025-10-30','2025-11-03'),  -- Nachfolger
  (4, 2, '2025-10-31','2025-11-04'),  -- Nachfolger
  (5, 3, '2025-11-01','2025-11-05'),  -- Nachfolger
  (6, 4, '2025-11-02','2025-11-06'),  -- Nachfolger
  (7, 5, '2025-11-03','2025-11-07'),  -- Nachfolger
  -- Zusätzliche Buchungen für den kritischen Zeitraum
  (8, 1, '2025-10-28','2025-10-31'),  -- Hotel Baur au Lac
  (1, 2, '2025-10-28','2025-10-31'),  -- Four Seasons
  (2, 3, '2025-10-28','2025-10-31'),  -- Grand Hotel National
  (3, 4, '2025-10-28','2025-10-31'),  -- Bellevue Palace
  (4, 5, '2025-10-28','2025-10-31');  -- Les Trois Rois

-- Rechnungen (5 Einträge)
INSERT INTO Invoice(booking_id, total_amount) VALUES
  (1, 240.00),
  (2, 360.00),
  (3, 600.00),
  (4, 440.00),
  (5, 500.00);

-- Rechnungen für Oktober-Buchungen
INSERT INTO Invoice(booking_id, total_amount) VALUES
  (6, 960.00),  -- 8 Nächte * 120.00
  (7, 540.00),  -- 3 Nächte * 180.00
  (8, 900.00),  -- 3 Nächte * 300.00
  (9, 660.00),  -- 3 Nächte * 220.00
  (10, 750.00), -- 3 Nächte * 250.00
  (11, 480.00), -- 4 Nächte * 120.00
  (12, 720.00), -- 4 Nächte * 180.00
  (13, 1200.00),-- 4 Nächte * 300.00
  (14, 880.00), -- 4 Nächte * 220.00
  (15, 1000.00),-- 4 Nächte * 250.00
  -- Rechnungen für die zusätzlichen Buchungen
  (16, 360.00), -- 3 Nächte * 120.00
  (17, 540.00), -- 3 Nächte * 180.00
  (18, 900.00), -- 3 Nächte * 300.00
  (19, 660.00), -- 3 Nächte * 220.00
  (20, 750.00); -- 3 Nächte * 250.00

COMMIT;
PRAGMA foreign_keys = ON;
"""

    print("Füge Beispieldaten ein...")
    cur.executescript(sql)
    conn.commit()
    conn.close()
    print("✅ Alle Tabellen wurden mit mindestens 5 Einträgen befüllt.")

if __name__ == '__main__':
    main()
