
# Chatbot - Nova

Dieser Chatbot wurde aus der ursprünglichen Website extrahiert, um eine eigenständige und fokussierte Interaktion zu ermöglichen. Die vollständige Historie der Änderungen, einschließlich der ursprünglichen Website-Integration, ist im Commit-Verlauf verfügbar. Diese Trennung erleichtert die Weiterentwicklung und Nutzung des Chatbots.

---

## **Funktionen des Chatbots**

Der Chatbot bietet folgende Funktionen:

1. **Verständnis natürlicher Sprache**: Er kann Benutzerfragen analysieren und basierend auf einer Datenbank, Webscraping oder KI-generierten Antworten reagieren.
2. **Integration einer Datenbank**: Der Bot greift auf eine SQLite-Datenbank zu, um häufig gestellte Fragen (FAQs) zu beantworten.
3. **Webscraping**: Der Chatbot durchsucht eine definierte Website, um relevante Antworten zu extrahieren, wenn keine direkte Datenbankübereinstimmung gefunden wird.
4. **Fuzzy-Matching**: Dank der Verwendung von `fuzzywuzzy` kann der Bot ähnliche Fragen erkennen und passende Antworten anbieten.
5. **Sprachunterstützung**: Er unterstützt Englisch und Deutsch, einschließlich automatischer Übersetzung mit `deep_translator`.
6. **KI-Antworten**: Bei fehlenden Datenbank- und Scraping-Antworten greift der Bot auf OpenAI (GPT) zurück.
7. **Memory-Funktion**: Der ChatBot speichert die letzten Konversationen ab um mit vergangenen Fragen zu interagieren über ChatGPT. 
8. **Automatische Datenbereinigung**: Alte Konversationsdaten werden regelmäßig entfernt, um die Datenbank sauber zu halten.


---

# **Lücken und Verbesserungsbedarf**

Obwohl der Chatbot bereits viele Funktionen bietet, gibt es Bereiche, die optimiert werden könnten:

1. **KI-Fallback**: 
   - Derzeit funktioniert das KI-Fallback noch nicht da man zuvor ein 'Billing' bei OpenAI einrichten muss.

2. **Fuzzy Matching**:
   - Die Ähnlichkeitsgrenze ist statisch auf 75 % eingestellt. Anpassungen oder dynamische Schwellenwerte könnten bessere Ergebnisse liefern.
   
3. **Fehlerbehandlung bei APIs**:
   - Robustere Fehlerbehandlung bei Übersetzungs- und KI-Anfragen wäre wünschenswert.

4. **Datenbank**:
   - Die Datenbank ist bis jetzt nur mit Beispielen zum Test gefüllt. 
   
5. **Performance**:
   - Aktuelle Datenbanklösungen sind für kleine Datenmengen geeignet, könnten jedoch bei großem Datenvolumen optimiert werden.

---

## **Anleitung zur Ausführung**

### Voraussetzungen

- **Python**: Version 3.9 oder höher
- **Abhängigkeiten**: Installiere die benötigten Python-Bibliotheken mit:
  ```bash
  pip install -r requirements.txt
  ```

### Schritte zur Ausführung

1. **Datenbank initialisieren**:
   Stelle sicher, dass die SQLite-Datenbank korrekt eingerichtet ist:
   ```python
   python -c "from Backup import init_db; init_db()"
   ```

2. **Chatbot starten**:
   Führe das Hauptskript aus:
   ```bash
   python Backup.py
   ```

3. **Zugriff auf die Benutzeroberfläche**:
   Öffne deinen Browser und navigiere zu:
   ```
   http://localhost:5001
   ```

4. **Integrationstest**:
   - Sende POST-Anfragen an `/ask` mit JSON-Daten wie:
     ```json
     {
       "question": "Was sind die Vorteile eures Produkts?",
       "language": "de"
     }
     ```

---

## **Commit-Verlauf**

Der Commit-Verlauf dokumentiert den gesamten Entwicklungsprozess, einschließlich:

- Der ursprünglichen Integration des Chatbots in die Website.
- Der späteren Extraktion des Chatbots als separates Modul.
- Verbesserungen und Bugfixes.

---
