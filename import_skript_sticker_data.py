# benötigte Bibliotheken importieren

import sqlite3
import pandas as pd
import os

# mit SQLite-Datenbank katzensticker.db verbinden und Zugangspunkt schaffen

conn = sqlite3.connect('katzensticker.db')
cur = conn.cursor()

# Daten aus CSV-Datei f. Katzenstickerdb auslesen und in Pandas einlesen

csv_datei = "katzensticker_daten.csv"
df = pd.read_csv("C:/Users/peppe/OneDrive/Desktop/Projects & Art/Katzensticker Database/katzensticker_daten.csv")

# Die ersten 5 Zeilen der Tabelle anzeigen

print(df.head())  

# Durch jede Zeile der CSV-Datei iterieren und die Daten in die Datenbank einfügen

for index, row in df.iterrows()
	bild_pfad = row['StickerBild']   # PNG-Bildpfad
	name = row['Name']				 # Sticker-Name
	emotion = row['Emotion']		 # Sticker-Emotion
	aktion = row['Aktion']			 # Sticker-Aktion

	# Fehlerbehandlung, Falls Fehler beim Einfügen auftritt
	try:
		# PNG-Bilddatei im binären Format öffnen und lesen
		with open(bild_pfad,'rb') as file:
			bild_daten = file.read()

		# Daten in Katzensticker-Datenbank einfügen und speichern
       cur.execute(
            """
            INSERT INTO katzensticker (StickerBild,Name,Emotion,Aktion)
            VALUES (?, ?, ?, ?)
            """, 
            (bild_daten, name, emotion, aktion)
        )

        # Änderungen in der Datenbank speichern
        conn.commit()

    except Exception as e:
        print(f"Fehler bei Zeile {index}:{e}")
        continue  # Fehler ignorieren und mit der nächsten Zeile fortfahren

# Verbindung zur Datenbank schließen
conn.close()