# database.py
import sqlite3

def fetch_person_data(person_id):
    try:
        conn = sqlite3.connect('fitness.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Person.Name, Person.Hight, Weight.Weight FROM Person JOIN Weight ON Person.Person_ID = Weight.Person_ID WHERE Person.Person_ID = ?', (person_id,))
        person_data = cursor.fetchone()
        conn.close()
        return person_data
    except sqlite3.Error as e:
        return f"SQLite error: {e}"

def add_person_data(name, hight, weight):
    try:
        conn = sqlite3.connect('fitness.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Person (Name, Hight) VALUES (?, ?)', (name, hight))
        person_id = cursor.lastrowid
        cursor.execute('INSERT INTO Weight (Person_ID, Weight) VALUES (?, ?)', (person_id, weight))
        conn.commit()
        conn.close()
        return person_id
    except sqlite3.Error as e:
        return f"SQLite error: {e}"
