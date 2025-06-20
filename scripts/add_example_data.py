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

    sql = """
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

-- Hotel Adressen (10 Einträge)
INSERT INTO Address(street, city, zip_code) VALUES
  ('Bahnhofstrasse 1',    'Zürich', '8001'),
  ('Langstrasse 60',      'Zürich', '8004'),
  ('Seefeldstrasse 20',   'Zürich', '8008'),
  ('Marktgasse 59',       'Bern',   '3011'),
  ('Freiestrasse 10',     'Basel',  '4051'),
  ('Rennweg 7',           'Zürich', '8001'),
  ('Talstrasse 1',        'Zürich', '8001'),
  ('Beethovenstrasse 21', 'Zürich', '8002'),
  ('Kurhausstrasse 65',   'Zürich', '8032'),
  ('Döltschiweg 240',     'Zürich', '8055');

-- Gäste (80 Einträge)
INSERT INTO Guest(first_name, last_name, email, birthday, nationality, address_id) VALUES
  -- Original 15 guests
  ('Max', 'Muster', 'max.muster@email.com', '1985-05-15', 'Switzerland', 11),
  ('Anna', 'Schmidt', 'anna.schmidt@email.com', '1990-08-22', 'Germany', 12),
  ('Thomas', 'Müller', 'thomas.mueller@email.com', '1988-03-10', 'Germany', 13),
  ('Laura', 'Weber', 'laura.weber@email.com', '1992-11-30', 'Switzerland', 14),
  ('Michael', 'Fischer', 'michael.fischer@email.com', '1987-07-18', 'Austria', 15),
  ('Sarah', 'Wagner', 'sarah.wagner@email.com', '1995-04-25', 'Germany', 16),
  ('David', 'Becker', 'david.becker@email.com', '1991-09-12', 'Switzerland', 17),
  ('Julia', 'Hoffmann', 'julia.hoffmann@email.com', '1989-12-05', 'Germany', 18),
  ('Peter', 'Schäfer', 'peter.schaefer@email.com', '1986-06-28', 'Austria', 19),
  ('Maria', 'Koch', 'maria.koch@email.com', '1993-02-14', 'Switzerland', 20),
  ('Franz', 'Bauer', 'franz.bauer@email.com', '1984-10-08', 'Germany', 21),
  ('Sophie', 'Richter', 'sophie.richter@email.com', '1994-07-20', 'Switzerland', 22),
  ('Lukas', 'Klein', 'lukas.klein@email.com', '1996-01-30', 'Germany', 23),
  ('Emma', 'Wolf', 'emma.wolf@email.com', '1990-11-15', 'Austria', 24),
  ('Noah', 'Schröder', 'noah.schroeder@email.com', '1988-08-03', 'Switzerland', 25),
  
  -- Additional 50 guests
  ('Emma', 'Johnson', 'emma.johnson@email.com', '1992-03-15', 'United Kingdom', 26),
  ('Lucas', 'Martin', 'lucas.martin@email.com', '1989-07-22', 'France', 27),
  ('Sophia', 'Rossi', 'sophia.rossi@email.com', '1991-11-30', 'Italy', 28),
  ('William', 'Garcia', 'william.garcia@email.com', '1987-05-18', 'Spain', 29),
  ('Olivia', 'Anderson', 'olivia.anderson@email.com', '1994-09-25', 'United States', 30),
  ('James', 'Wilson', 'james.wilson@email.com', '1986-12-10', 'United Kingdom', 31),
  ('Isabella', 'Brown', 'isabella.brown@email.com', '1993-02-28', 'United States', 32),
  ('Benjamin', 'Taylor', 'benjamin.taylor@email.com', '1990-08-15', 'United Kingdom', 33),
  ('Mia', 'Thomas', 'mia.thomas@email.com', '1995-06-20', 'United States', 34),
  ('Ethan', 'Moore', 'ethan.moore@email.com', '1988-04-12', 'United Kingdom', 35),
  ('Charlotte', 'Lee', 'charlotte.lee@email.com', '1992-10-05', 'United States', 36),
  ('Alexander', 'White', 'alexander.white@email.com', '1989-01-25', 'United Kingdom', 37),
  ('Amelia', 'Harris', 'amelia.harris@email.com', '1994-07-30', 'United States', 38),
  ('Daniel', 'Clark', 'daniel.clark@email.com', '1991-03-18', 'United Kingdom', 39),
  ('Ava', 'Lewis', 'ava.lewis@email.com', '1987-11-22', 'United States', 40),
  ('Matthew', 'Robinson', 'matthew.robinson@email.com', '1993-09-14', 'United Kingdom', 41),
  ('Sofia', 'Walker', 'sofia.walker@email.com', '1990-05-28', 'United States', 42),
  ('David', 'Young', 'david.young@email.com', '1988-12-03', 'United Kingdom', 43),
  ('Victoria', 'Allen', 'victoria.allen@email.com', '1995-02-17', 'United States', 44),
  ('Joseph', 'King', 'joseph.king@email.com', '1992-08-09', 'United Kingdom', 45),
  ('Grace', 'Wright', 'grace.wright@email.com', '1989-06-24', 'United States', 46),
  ('Samuel', 'Lopez', 'samuel.lopez@email.com', '1994-04-11', 'Spain', 47),
  ('Chloe', 'Hill', 'chloe.hill@email.com', '1991-10-19', 'United Kingdom', 48),
  ('Henry', 'Scott', 'henry.scott@email.com', '1987-07-31', 'United States', 49),
  ('Zoe', 'Green', 'zoe.green@email.com', '1993-01-13', 'United Kingdom', 50),
  ('Sebastian', 'Adams', 'sebastian.adams@email.com', '1990-09-27', 'United States', 51),
  ('Lily', 'Baker', 'lily.baker@email.com', '1988-03-08', 'United Kingdom', 52),
  ('Jack', 'Gonzalez', 'jack.gonzalez@email.com', '1995-11-21', 'Spain', 53),
  ('Hannah', 'Nelson', 'hannah.nelson@email.com', '1992-05-16', 'United States', 54),
  ('Owen', 'Carter', 'owen.carter@email.com', '1989-12-29', 'United Kingdom', 55),
  ('Aria', 'Mitchell', 'aria.mitchell@email.com', '1994-08-07', 'United States', 56),
  ('Gabriel', 'Perez', 'gabriel.perez@email.com', '1991-04-23', 'Spain', 57),
  ('Scarlett', 'Roberts', 'scarlett.roberts@email.com', '1987-10-14', 'United Kingdom', 58),
  ('Carter', 'Turner', 'carter.turner@email.com', '1993-06-30', 'United States', 59),
  ('Aubrey', 'Phillips', 'aubrey.phillips@email.com', '1990-02-11', 'United Kingdom', 60),
  ('Ryan', 'Campbell', 'ryan.campbell@email.com', '1988-07-25', 'United States', 61),
  ('Nora', 'Parker', 'nora.parker@email.com', '1995-01-19', 'United Kingdom', 62),
  ('Nathan', 'Evans', 'nathan.evans@email.com', '1992-09-03', 'United States', 63),
  ('Ellie', 'Edwards', 'ellie.edwards@email.com', '1989-05-17', 'United Kingdom', 64),
  ('Isaac', 'Collins', 'isaac.collins@email.com', '1994-11-28', 'United States', 65),
  
  -- Additional 15 guests
  ('Liam', 'Murphy', 'liam.murphy@email.com', '1991-07-14', 'Ireland', 66),
  ('Eva', 'Andersen', 'eva.andersen@email.com', '1988-12-03', 'Denmark', 67),
  ('Lars', 'Berg', 'lars.berg@email.com', '1993-04-22', 'Norway', 68),
  ('Anna', 'Lindberg', 'anna.lindberg@email.com', '1990-09-17', 'Sweden', 69),
  ('Jan', 'Kowalski', 'jan.kowalski@email.com', '1987-03-29', 'Poland', 70),
  ('Maria', 'Nowak', 'maria.nowak@email.com', '1994-11-08', 'Poland', 71),
  ('Hans', 'Müller', 'hans.muller@email.com', '1989-06-25', 'Germany', 72),
  ('Sophie', 'Dubois', 'sophie.dubois@email.com', '1992-02-19', 'France', 73),
  ('Marco', 'Bianchi', 'marco.bianchi@email.com', '1995-08-11', 'Italy', 74),
  ('Laura', 'Santos', 'laura.santos@email.com', '1991-01-30', 'Portugal', 75),
  ('Carlos', 'Rodriguez', 'carlos.rodriguez@email.com', '1988-05-07', 'Spain', 76),
  ('Emma', 'Jensen', 'emma.jensen@email.com', '1993-10-24', 'Denmark', 77),
  ('Oscar', 'Nilsson', 'oscar.nilsson@email.com', '1990-12-15', 'Sweden', 78),
  ('Lena', 'Schmidt', 'lena.schmidt@email.com', '1994-07-03', 'Germany', 79),
  ('Thomas', 'Anderson', 'thomas.anderson@email.com', '1989-04-28', 'United Kingdom', 80);

-- Gäste Adressen (80 Einträge)
INSERT INTO Address(street, city, zip_code) VALUES
  -- Original 15 addresses
  ('Hauptstrasse 10',     'Zürich', '8002'),
  ('Bahnhofplatz 5',      'Zürich', '8001'),
  ('Limmatquai 20',       'Zürich', '8001'),
  ('Bundesgasse 15',      'Bern',   '3011'),
  ('Aeschenvorstadt 30',  'Basel',  '4051'),
  ('Rämistrasse 25',      'Zürich', '8001'),
  ('Kornhausstrasse 8',   'Bern',   '3011'),
  ('Steinenvorstadt 12',  'Basel',  '4051'),
  ('Löwenstrasse 45',     'Zürich', '8001'),
  ('Marktgasse 12',       'Bern',   '3011'),
  ('Freie Strasse 8',     'Basel',  '4051'),
  ('Bahnhofstrasse 30',   'Zürich', '8001'),
  ('Bundesgasse 20',      'Bern',   '3011'),
  ('Aeschenvorstadt 40',  'Basel',  '4051'),
  ('Rämistrasse 35',      'Zürich', '8001'),
  
  -- Additional 50 addresses
  ('Bahnhofstrasse 40',   'Zürich', '8001'),
  ('Limmatquai 30',       'Zürich', '8001'),
  ('Bundesgasse 25',      'Bern',   '3011'),
  ('Aeschenvorstadt 50',  'Basel',  '4051'),
  ('Rämistrasse 45',      'Zürich', '8001'),
  ('Kornhausstrasse 18',  'Bern',   '3011'),
  ('Steinenvorstadt 22',  'Basel',  '4051'),
  ('Löwenstrasse 55',     'Zürich', '8001'),
  ('Marktgasse 22',       'Bern',   '3011'),
  ('Freie Strasse 18',    'Basel',  '4051'),
  ('Bahnhofstrasse 50',   'Zürich', '8001'),
  ('Limmatquai 40',       'Zürich', '8001'),
  ('Bundesgasse 35',      'Bern',   '3011'),
  ('Aeschenvorstadt 60',  'Basel',  '4051'),
  ('Rämistrasse 55',      'Zürich', '8001'),
  ('Kornhausstrasse 28',  'Bern',   '3011'),
  ('Steinenvorstadt 32',  'Basel',  '4051'),
  ('Löwenstrasse 65',     'Zürich', '8001'),
  ('Marktgasse 32',       'Bern',   '3011'),
  ('Freie Strasse 28',    'Basel',  '4051'),
  ('Bahnhofstrasse 60',   'Zürich', '8001'),
  ('Limmatquai 50',       'Zürich', '8001'),
  ('Bundesgasse 45',      'Bern',   '3011'),
  ('Aeschenvorstadt 70',  'Basel',  '4051'),
  ('Rämistrasse 65',      'Zürich', '8001'),
  ('Kornhausstrasse 38',  'Bern',   '3011'),
  ('Steinenvorstadt 42',  'Basel',  '4051'),
  ('Löwenstrasse 75',     'Zürich', '8001'),
  ('Marktgasse 42',       'Bern',   '3011'),
  ('Freie Strasse 38',    'Basel',  '4051'),
  ('Bahnhofstrasse 70',   'Zürich', '8001'),
  ('Limmatquai 60',       'Zürich', '8001'),
  ('Bundesgasse 55',      'Bern',   '3011'),
  ('Aeschenvorstadt 80',  'Basel',  '4051'),
  ('Rämistrasse 75',      'Zürich', '8001'),
  ('Kornhausstrasse 48',  'Bern',   '3011'),
  ('Steinenvorstadt 52',  'Basel',  '4051'),
  ('Löwenstrasse 85',     'Zürich', '8001'),
  ('Marktgasse 52',       'Bern',   '3011'),
  ('Freie Strasse 48',    'Basel',  '4051'),
  ('Bahnhofstrasse 80',   'Zürich', '8001'),
  ('Limmatquai 70',       'Zürich', '8001'),
  ('Bundesgasse 65',      'Bern',   '3011'),
  ('Aeschenvorstadt 90',  'Basel',  '4051'),
  ('Rämistrasse 85',      'Zürich', '8001'),
  ('Kornhausstrasse 58',  'Bern',   '3011'),
  ('Steinenvorstadt 62',  'Basel',  '4051'),
  ('Löwenstrasse 95',     'Zürich', '8001'),
  ('Marktgasse 62',       'Bern',   '3011'),
  ('Freie Strasse 58',    'Basel',  '4051'),
  
  -- Additional 15 addresses
  ('Bahnhofstrasse 90',   'Zürich', '8001'),
  ('Limmatquai 80',       'Zürich', '8001'),
  ('Bundesgasse 75',      'Bern',   '3011'),
  ('Aeschenvorstadt 100', 'Basel',  '4051'),
  ('Rämistrasse 95',      'Zürich', '8001'),
  ('Kornhausstrasse 68',  'Bern',   '3011'),
  ('Steinenvorstadt 72',  'Basel',  '4051'),
  ('Löwenstrasse 105',    'Zürich', '8001'),
  ('Marktgasse 72',       'Bern',   '3011'),
  ('Freie Strasse 68',    'Basel',  '4051'),
  ('Bahnhofstrasse 100',  'Zürich', '8001'),
  ('Limmatquai 90',       'Zürich', '8001'),
  ('Bundesgasse 85',      'Bern',   '3011'),
  ('Aeschenvorstadt 110', 'Basel',  '4051'),
  ('Rämistrasse 105',     'Zürich', '8001');

-- Hotels (10 Einträge)
INSERT INTO Hotel(name, stars, address_id) VALUES
  ('Hotel Baur au Lac', 5, 1),        -- Bahnhofstrasse 1
  ('Four Seasons', 5, 2),             -- Langstrasse 60
  ('Grand Hotel National', 5, 3),     -- Seefeldstrasse 20
  ('Bellevue Palace', 5, 4),          -- Marktgasse 59
  ('Les Trois Rois', 5, 5),           -- Freiestrasse 10
  ('Widder Hotel', 3, 6),             -- Rennweg 7
  ('Hotel Messia', 2, 7),             -- Talstrasse 1
  ('Park Hyatt Zürich', 4, 8),        -- Beethovenstrasse 21
  ('The Dolder Grand', 5, 9),         -- Kurhausstrasse 65
  ('Atlantis by Giardino', 3, 10);    -- Döltschiweg 240

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

-- Zimmer (80 Einträge)
INSERT INTO Room(hotel_id, room_number, type_id, price_per_night) VALUES
  -- Original 50 rooms (1-5)
  -- Hotel Baur au Lac (15 rooms)
  (1, '101', 1, 120.00),
  (1, '102', 2, 180.00),
  (1, '103', 2, 180.00),
  (1, '104', 3, 250.00),
  (1, '105', 3, 250.00),
  (1, '106', 5, 500.00),
  (1, '107', 2, 180.00),
  (1, '108', 2, 180.00),
  (1, '109', 3, 250.00),
  (1, '110', 3, 250.00),
  (1, '111', 4, 350.00),
  (1, '112', 4, 350.00),
  (1, '113', 5, 500.00),
  (1, '114', 5, 500.00),
  (1, '115', 5, 500.00),
  
  -- Four Seasons (12 rooms)
  (2, '201', 2, 200.00),
  (2, '202', 2, 200.00),
  (2, '203', 3, 280.00),
  (2, '204', 3, 280.00),
  (2, '205', 5, 550.00),
  (2, '206', 2, 200.00),
  (2, '207', 3, 280.00),
  (2, '208', 4, 400.00),
  (2, '209', 4, 400.00),
  (2, '210', 5, 550.00),
  (2, '211', 5, 550.00),
  (2, '212', 5, 550.00),
  
  -- Grand Hotel National (8 rooms)
  (3, '301', 2, 190.00),
  (3, '302', 2, 190.00),
  (3, '303', 3, 260.00),
  (3, '304', 3, 260.00),
  (3, '305', 5, 520.00),
  (3, '306', 4, 380.00),
  (3, '307', 4, 380.00),
  (3, '308', 5, 520.00),
  
  -- Bellevue Palace (7 rooms)
  (4, '301', 2, 195.00),
  (4, '302', 2, 195.00),
  (4, '303', 3, 270.00),
  (4, '304', 3, 270.00),
  (4, '305', 5, 530.00),
  (4, '306', 4, 390.00),
  (4, '307', 5, 530.00),
  
  -- Les Trois Rois (8 rooms)
  (5, '301', 2, 210.00),
  (5, '302', 2, 210.00),
  (5, '303', 3, 290.00),
  (5, '304', 3, 290.00),
  (5, '305', 5, 540.00),
  (5, '306', 4, 410.00),
  (5, '307', 4, 410.00),
  (5, '308', 5, 540.00),

  -- New Hotels (6-10)
  -- Widder Hotel (6 rooms)
  (6, '101', 2, 220.00),
  (6, '102', 2, 220.00),
  (6, '103', 3, 320.00),
  (6, '104', 4, 420.00),
  (6, '105', 5, 580.00),
  (6, '106', 5, 580.00),

  -- Baur au Lac (6 rooms)
  (7, '101', 2, 230.00),
  (7, '102', 2, 230.00),
  (7, '103', 3, 330.00),
  (7, '104', 4, 430.00),
  (7, '105', 5, 590.00),
  (7, '106', 5, 590.00),

  -- Park Hyatt Zürich (6 rooms)
  (8, '101', 2, 240.00),
  (8, '102', 2, 240.00),
  (8, '103', 3, 340.00),
  (8, '104', 4, 440.00),
  (8, '105', 5, 600.00),
  (8, '106', 5, 600.00),

  -- The Dolder Grand (6 rooms)
  (9, '101', 2, 250.00),
  (9, '102', 2, 250.00),
  (9, '103', 3, 350.00),
  (9, '104', 4, 450.00),
  (9, '105', 5, 650.00),
  (9, '106', 5, 650.00),

  -- Atlantis by Giardino (6 rooms)
  (10, '101', 2, 260.00),
  (10, '102', 2, 260.00),
  (10, '103', 3, 360.00),
  (10, '104', 4, 460.00),
  (10, '105', 5, 660.00),
  (10, '106', 5, 660.00);

-- Room_Facilities (5 Einträge)
INSERT INTO Room_Facilities(room_id, facility_id) VALUES
  -- Original 5 rooms with their facilities
  (1,1),(2,2),(3,3),(4,4),(5,5),
  -- Additional rooms with random facilities
  (6,1),(6,3),(6,5),
  (7,2),(7,4),
  (8,1),(8,5),
  (9,2),(9,3),(9,4),
  (10,1),(10,2),(10,5),
  (11,3),(11,4),
  (12,1),(12,2),(12,3),
  (13,4),(13,5),
  (14,1),(14,3),(14,5),
  (15,2),(15,4),
  (16,1),(16,5),
  (17,2),(17,3),(17,4),
  (18,1),(18,2),(18,5),
  (19,3),(19,4),
  (20,1),(20,2),(20,3),
  (21,4),(21,5),
  (22,1),(22,3),(22,5),
  (23,2),(23,4),
  (24,1),(24,5),
  (25,2),(25,3),(25,4),
  (26,1),(26,2),(26,5),
  (27,3),(27,4),
  (28,1),(28,2),(28,3),
  (29,4),(29,5),
  (30,1),(30,3),(30,5),
  (31,2),(31,4),
  (32,1),(32,5),
  (33,2),(33,3),(33,4),
  (34,1),(34,2),(34,5),
  (35,3),(35,4),
  (36,1),(36,2),(36,3),
  (37,4),(37,5),
  (38,1),(38,3),(38,5),
  (39,2),(39,4),
  (40,1),(40,5),
  (41,2),(41,3),(41,4),
  (42,1),(42,2),(42,5),
  (43,3),(43,4),
  (44,1),(44,2),(44,3),
  (45,4),(45,5),
  (46,1),(46,3),(46,5),
  (47,2),(47,4),
  (48,1),(48,5),
  (49,2),(49,3),(49,4),
  (50,1),(50,2),(50,5),
  (51,3),(51,4),
  (52,1),(52,2),(52,3),
  (53,4),(53,5),
  (54,1),(54,3),(54,5),
  (55,2),(55,4),
  (56,1),(56,5),
  (57,2),(57,3),(57,4),
  (58,1),(58,2),(58,5),
  (59,3),(59,4),
  (60,1),(60,2),(60,3),
  (61,4),(61,5),
  (62,1),(62,3),(62,5),
  (63,2),(63,4),
  (64,1),(64,5),
  (65,2),(65,3),(65,4),
  (66,1),(66,2),(66,5),
  (67,3),(67,4),
  (68,1),(68,2),(68,3),
  (69,4),(69,5),
  (70,1),(70,3),(70,5),
  (71,2),(71,4),
  (72,1),(72,5),
  (73,2),(73,3),(73,4),
  (74,1),(74,2),(74,5),
  (75,3),(75,4),
  (76,1),(76,2),(76,3),
  (77,4),(77,5),
  (78,1),(78,3),(78,5),
  (79,2),(79,4),
  (80,1),(80,5);

-- Buchungen (90 Einträge)
INSERT INTO Booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount, rating, recommendation) VALUES
  -- Original 5 bookings
  (1, 1, '2025-05-20','2025-05-22', 0, 240.0, NULL, NULL),
  (2, 2, '2025-06-01','2025-06-03', 0, 360.0, 7, NULL),
  (3, 3, '2025-07-10','2025-07-12', 0, 360.0, 10, 'Best hotel experience ever!'),
  (4, 4, '2025-08-05','2025-08-07', 1, 280.0, NULL, NULL),
  (5, 5, '2025-08-20','2025-08-22', 0, 500.0, 6, 'Good but could be better.'),
  
  -- Second bookings for first 5 guests (rooms 1-5) around 28.10.2025
  (1, 1, '2025-10-25','2025-11-02', 0, 960.0, 9, 'Excellent service and beautiful rooms!'),
  (2, 2, '2025-10-26','2025-11-03', 0, 1440.0, 7, NULL),
  (3, 3, '2025-10-27','2025-11-04', 0, 1440.0, 10, 'Best hotel experience ever!'),
  (4, 4, '2025-10-28','2025-11-05', 0, 2000.0, 8, 'Great stay'),
  (5, 5, '2025-10-28','2025-11-06', 0, 2250.0, 6, 'Good but could be better.'),
  
  -- New bookings for all 80 guests (with varying dates around 28.10-31.10.2025)
  (6, 6, '2025-10-25','2025-11-02', 0, 4000.0, 8, 'Very comfortable stay'),
  (7, 7, '2025-10-26','2025-11-03', 0, 1440.0, 9, 'Great location'),
  (8, 8, '2025-10-27','2025-11-04', 0, 1440.0, 7, NULL),
  (9, 9, '2025-10-28','2025-11-05', 0, 2000.0, 10, 'Perfect service'),
  (10, 10, '2025-10-28','2025-11-06', 0, 2250.0, 8, 'Would come again'),
  (11, 11, '2025-10-25','2025-11-02', 0, 2800.0, 9, 'Excellent experience'),
  (12, 12, '2025-10-26','2025-11-03', 0, 2800.0, 7, 'Nice hotel'),
  (13, 13, '2025-10-27','2025-11-04', 0, 4000.0, 8, 'Good value'),
  (14, 14, '2025-10-28','2025-11-05', 0, 4000.0, 9, 'Great staff'),
  (15, 15, '2025-10-28','2025-11-06', 0, 4500.0, 10, 'Best hotel ever'),
  (16, 16, '2025-10-25','2025-11-02', 0, 1600.0, 8, 'Comfortable rooms'),
  (17, 17, '2025-10-26','2025-11-03', 0, 1600.0, 7, NULL),
  (18, 18, '2025-10-27','2025-11-04', 0, 2240.0, 9, 'Excellent service'),
  (19, 19, '2025-10-28','2025-11-05', 0, 2240.0, 8, 'Great location'),
  (20, 20, '2025-10-28','2025-11-06', 0, 4950.0, 10, 'Perfect stay'),
  (21, 21, '2025-10-25','2025-11-02', 0, 1600.0, 7, 'Nice hotel'),
  (22, 22, '2025-10-26','2025-11-03', 0, 2240.0, 9, 'Would recommend'),
  (23, 23, '2025-10-27','2025-11-04', 0, 3200.0, 8, 'Great experience'),
  (24, 24, '2025-10-28','2025-11-05', 0, 3200.0, 10, 'Best service'),
  (25, 25, '2025-10-28','2025-11-06', 0, 4950.0, 7, NULL),
  (26, 26, '2025-10-25','2025-11-02', 0, 4400.0, 9, 'Excellent stay'),
  (27, 27, '2025-10-26','2025-11-03', 0, 4400.0, 8, 'Great hotel'),
  (28, 28, '2025-10-27','2025-11-04', 0, 1520.0, 10, 'Perfect experience'),
  (29, 29, '2025-10-28','2025-11-05', 0, 1520.0, 7, 'Nice staff'),
  (30, 30, '2025-10-28','2025-11-06', 0, 2340.0, 9, 'Would come again'),
  (31, 31, '2025-10-25','2025-11-02', 0, 2080.0, 8, 'Great location'),
  (32, 32, '2025-10-26','2025-11-03', 0, 4160.0, 10, 'Best hotel'),
  (33, 33, '2025-10-27','2025-11-04', 0, 3040.0, 7, NULL),
  (34, 34, '2025-10-28','2025-11-05', 0, 3040.0, 9, 'Excellent service'),
  (35, 35, '2025-10-28','2025-11-06', 0, 4680.0, 8, 'Great stay'),
  (36, 36, '2025-10-25','2025-11-02', 0, 1560.0, 10, 'Perfect experience'),
  (37, 37, '2025-10-26','2025-11-03', 0, 1560.0, 7, 'Nice hotel'),
  (38, 38, '2025-10-27','2025-11-04', 0, 2160.0, 9, 'Would recommend'),
  (39, 39, '2025-10-28','2025-11-05', 0, 2160.0, 8, 'Great service'),
  (40, 40, '2025-10-28','2025-11-06', 0, 4770.0, 10, 'Best stay ever'),
  (41, 41, '2025-10-25','2025-11-02', 0, 3120.0, 7, NULL),
  (42, 42, '2025-10-26','2025-11-03', 0, 4240.0, 9, 'Excellent hotel'),
  (43, 43, '2025-10-27','2025-11-04', 0, 1680.0, 8, 'Great location'),
  (44, 44, '2025-10-28','2025-11-05', 0, 1680.0, 10, 'Perfect service'),
  (45, 45, '2025-10-28','2025-11-06', 0, 2610.0, 7, 'Nice stay'),
  (46, 46, '2025-10-25','2025-11-02', 0, 2320.0, 9, 'Would come again'),
  (47, 47, '2025-10-26','2025-11-03', 0, 4320.0, 8, 'Great experience'),
  (48, 48, '2025-10-27','2025-11-04', 0, 3280.0, 10, 'Best hotel'),
  (49, 49, '2025-10-28','2025-11-05', 0, 3280.0, 7, NULL),
  (50, 50, '2025-10-28','2025-11-06', 0, 4860.0, NULL, NULL),
  (51, 51, '2025-10-25','2025-11-02', 0, 1760.0, NULL, NULL),
  (52, 52, '2025-10-26','2025-11-03', 0, 1760.0, NULL, NULL),
  (53, 53, '2025-10-27','2025-11-04', 0, 2560.0, NULL, NULL),
  (54, 54, '2025-10-28','2025-11-05', 0, 3360.0, NULL, NULL),
  (55, 55, '2025-10-28','2025-11-06', 0, 5220.0, NULL, NULL),
  (56, 56, '2025-10-25','2025-11-02', 0, 4640.0, NULL, NULL),
  (57, 57, '2025-10-26','2025-11-03', 0, 1840.0, NULL, NULL),
  (58, 58, '2025-10-27','2025-11-04', 0, 1840.0, NULL, NULL),
  (59, 59, '2025-10-28','2025-11-05', 0, 2640.0, 8, 'Great location'),
  (60, 60, '2025-10-28','2025-11-06', 0, 3870.0, 10, 'Perfect service'),
  (61, 61, '2025-10-25','2025-11-02', 0, 4720.0, 7, 'Nice stay'),
  (62, 62, '2025-10-26','2025-11-03', 0, 4720.0, 9, 'Would come again'),
  (63, 63, '2025-10-27','2025-11-04', 0, 1920.0, 8, 'Great experience'),
  (64, 64, '2025-10-28','2025-11-05', 0, 1920.0, 10, 'Best hotel'),
  (65, 65, '2025-10-28','2025-11-06', 0, 3060.0, 7, NULL),
  (66, 66, '2025-10-25','2025-11-02', 0, 3520.0, 9, 'Excellent service'),
  (67, 67, '2025-10-26','2025-11-03', 0, 4800.0, 8, 'Great stay'),
  (68, 68, '2025-10-27','2025-11-04', 0, 4800.0, 10, 'Perfect experience'),
  (69, 69, '2025-10-28','2025-11-05', 0, 2000.0, 7, 'Nice hotel'),
  (70, 70, '2025-10-28','2025-11-06', 0, 2250.0, 9, 'Would recommend'),
  (71, 71, '2025-10-25','2025-11-02', 0, 2800.0, 8, 'Great service'),
  (72, 72, '2025-10-26','2025-11-03', 0, 3600.0, 10, 'Best stay ever'),
  (73, 73, '2025-10-27','2025-11-04', 0, 5200.0, 7, NULL),
  (74, 74, '2025-10-28','2025-11-05', 0, 5200.0, 9, 'Excellent hotel'),
  (75, 75, '2025-10-28','2025-11-06', 0, 2340.0, 8, 'Great location'),
  (76, 76, '2025-10-25','2025-11-02', 0, 2080.0, 10, 'Perfect service'),
  (77, 77, '2025-10-26','2025-11-03', 0, 2880.0, 7, 'Nice stay'),
  (78, 78, '2025-10-27','2025-11-04', 0, 3680.0, 9, 'Would come again'),
  (79, 79, '2025-10-28','2025-11-05', 0, 5280.0, 8, 'Great experience'),
  (80, 80, '2025-10-28','2025-11-06', 0, 5940.0, 10, 'Best hotel');

-- Rechnungen (5 Einträge)
INSERT INTO Invoice(booking_id, total_amount) VALUES
  (1, 240.00),
  (2, 360.00),
  (3, 360.00),
  (5, 500.00);

-- Rechnungen für Oktober-Buchungen
INSERT INTO Invoice(booking_id, total_amount) VALUES
  -- Buchungen 6-10 
  (6, 960.00),  
  (7, 1440.00),  
  (8, 1440.00),  
  (9, 2000.00),  
  (10, 2250.00), 
  
  -- Buchungen 11-15 
  (11, 4000.00),  
  (12, 1440.00),  
  (13, 1440.00), 
  (14, 2000.00),  
  (15, 2250.00), 
  
  -- Buchungen 16-20 
  (16, 2800.00),  
  (17, 2800.00),  
  (18, 4000.00), 
  (19, 4000.00), 
  (20, 4500.00), 
  
  -- Buchungen 21-25 
  (21, 1600.00),  
  (22, 1600.00), 
  (23, 2240.00), 
  (24, 2240.00), 
  (25, 4950.00), 
  
  -- Buchungen 26-30 
  (26, 1600.00), 
  (27, 2240.00), 
  (28, 3200.00), 
  (29, 3200.00), 
  (30, 4950.00),
  
  -- Buchungen 31-35 
  (31, 4400.00),  
  (32, 4400.00), 
  (33, 1520.00), 
  (34, 1520.00), 
  (35, 2340.00), 
  
  -- Buchungen 36-40 
  (36, 2080.00), 
  (37, 4160.00), 
  (38, 3040.00), 
  (39, 3040.00), 
  (40, 4680.00), 
  
  -- Buchungen 41-45 
  (41, 1560.00), 
  (42, 1560.00), 
  (43, 2160.00), 
  (44, 2160.00), 
  (45, 4770.00), 
  
  -- Buchungen 46-50 
  (46, 3120.00), 
  (47, 4240.00), 
  (48, 1680.00),
  (49, 1680.00), 
  (50, 2610.00), 
  
  -- Buchungen 51-55 
  (51, 2320.00), 
  (52, 4320.00),
  (53, 3280.00), 
  (54, 3280.00), 
  (55, 4860.00), 
  
  -- Buchungen 56-60 
  (56, 1760.00), 
  (57, 1760.00), 
  (58, 2560.00), 
  (59, 3360.00), 
  (60, 5220.00), 
  
  -- Buchungen 61-65 
  (61, 4640.00), 
  (62, 1840.00), 
  (63, 1840.00),
  (64, 2640.00), 
  (65, 3870.00), 
  
  -- Buchungen 66-70 
  (66, 4720.00), 
  (67, 4720.00), 
  (68, 1920.00), 
  (69, 1920.00), 
  (70, 3060.00),
  
  -- Buchungen 71-75 
  (71, 3520.00), 
  (72, 4800.00), 
  (73, 4800.00), 
  (74, 2000.00), 
  (75, 2250.00), 
  
  -- Buchungen 76-80 
  (76, 2800.00), 
  (77, 3600.00), 
  (78, 5200.00), 
  (79, 5200.00), 
  (80, 2340.00),
  
  -- Buchungen 81-85
  (81, 2080),
  (82, 2880),
  (83, 3680),
  (84, 5280),
  (85, 5940);

COMMIT;

PRAGMA foreign_keys = ON;
"""

    cur.executescript(sql)
    conn.commit()
    conn.close()
    print("✅ The Databank got reset back to original state.")

if __name__ == '__main__':
    main()
