# benötigte Bibliotheken importieren

import sqlite3
import pandas as pd
import os

# mit SQLite-Datenbank katzensticker.db verbinden und Zugangspunkt

conn = sqlite3.connect('katzensticker.db')
cur = conn.cursor()

# Daten aus CSV-Datei f. Katzenstickerdb auslesen und in Pandas einlesen

csv_datei = "katzensticker_daten.csv"
df = pd.read_csv("C:/Users/peppe/OneDrive/Desktop/Projects & Art/Katzensticker Database/katzensticker_daten.csv")

# Die ersten 5 Zeilen der Tabelle anzeigen

print(df.head())  
