import sqlite3
import os

# Definiere den Pfad zur FAQ.db
db_path = os.path.join(os.getcwd(), 'FAQ.db')

# Stelle sicher, dass der Ordner 'Test' existiert
if not os.path.exists(os.path.dirname(db_path)):
    os.makedirs(os.path.dirname(db_path))  # Erstelle den Ordner, falls er nicht existiert

def add_faq_entry(question, answer):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT OR IGNORE INTO faq (question, answer) VALUES (?, ?)", (question, answer))
        conn.commit()
        print(f"Die Frage '{question}' und die Antwort wurden erfolgreich hinzugefügt.")
    except sqlite3.Error as e:
        print(f"Fehler beim Hinzufügen der Daten: {e}")
    finally:
        conn.close()

def list_faq_entries():
    """
    Listet alle Fragen mit ihren IDs auf, um dem Benutzer die Auswahl zum Löschen zu ermöglichen.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, question FROM faq")
        rows = cursor.fetchall()

        if rows:
            print("Verfügbare Fragen zum Löschen:")
            for row in rows:
                print(f"ID: {row[0]} - Frage: {row[1]}")
        else:
            print("Keine Fragen in der Datenbank gefunden.")
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
    finally:
        conn.close()

def delete_faq_entries_by_ids(entry_ids):
    """
    Löscht mehrere Fragen basierend auf den angegebenen IDs.
    
    Args:
        entry_ids (list[int]): Eine Liste von IDs, die gelöscht werden sollen.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.executemany("DELETE FROM faq WHERE id = ?", [(entry_id,) for entry_id in entry_ids])
        conn.commit()
        print(f"Einträge mit IDs {', '.join(map(str, entry_ids))} wurden erfolgreich gelöscht.")
    except sqlite3.Error as e:
        print(f"Fehler beim Löschen der Daten: {e}")
    finally:
        conn.close()

def create_faq_table():
    """
    Erstellt die FAQ-Tabelle, falls sie noch nicht existiert.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS faq (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            question TEXT NOT NULL,
                            answer TEXT NOT NULL)''')
        conn.commit()
        print("Tabelle 'faq' wurde erstellt.")
    except sqlite3.Error as e:
        print(f"Fehler beim Erstellen der Tabelle: {e}")
    finally:
        conn.close()

# Wenn du sicherstellen willst, dass die Tabelle erstellt wird:
create_faq_table()

if __name__ == "__main__":
    print("Wähle eine Option:")
    print("1: Neue Frage und Antwort hinzufügen")
    print("2: Frage und Antwort löschen")
    option = input("Option (1/2): ")

    if option == "1":
        question = input("Gib die Frage ein: ")
        answer = input("Gib die Antwort ein: ")
        add_faq_entry(question, answer)
    elif option == "2":
        # Zuerst alle Fragen mit IDs auflisten
        list_faq_entries()
        
        # IDs der zu löschenden Fragen eingeben (kommagetrennt)
        try:
            ids_input = input("Gib die IDs der Fragen ein, die du löschen möchtest (kommagetrennt): ")
            entry_ids = [int(entry_id.strip()) for entry_id in ids_input.split(",")]
            delete_faq_entries_by_ids(entry_ids)
        except ValueError:
            print("Ungültige IDs eingegeben. Bitte Zahlen eingeben, getrennt durch Kommas.")
    else:
        print("Ungültige Option.")
