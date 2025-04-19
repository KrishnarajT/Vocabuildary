import sqlite3
import csv
import os

DB_FILE = 'vocab.db'
CSV_FILE = 'words.csv'

def initialize_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE,
            meaning TEXT,
            example TEXT,
            sent INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def import_words_from_csv(csv_file):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    added_count = 0
    skipped_count = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                c.execute('''
                    INSERT INTO words (word, meaning, example)
                    VALUES (?, ?, ?)
                ''', (row['word'], row['meaning'], row['example']))
                added_count += 1
            except sqlite3.IntegrityError:
                skipped_count += 1  # Word already exists

    conn.commit()
    conn.close()

    print(f"✅ Import complete: {added_count} new words added, {skipped_count} duplicates skipped.")

if __name__ == "__main__":
    initialize_db()
    import_words_from_csv(CSV_FILE)
