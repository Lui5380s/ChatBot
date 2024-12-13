
# ChatBot - Nova

Der ChatBot wurde aus einer früheren Version extrahiert und bietet eine fokussierte Interaktion mit Benutzern. Die komplette Historie der Änderungen ist im Commit-Verlauf verfügbar, was eine klare Trennung der früheren Website-Integration ermöglicht und die Weiterentwicklung vereinfacht.

---

## **Funktionen des ChatBots**

Der ChatBot bietet folgende Funktionen:

1. **Verständnis natürlicher Sprache**: Der ChatBot kann Benutzerfragen analysieren und entsprechende Antworten basierend auf einer Datenbank oder Webscraping bereitstellen.
2. **Integration einer Datenbank**: Der Bot nutzt eine SQLite-Datenbank, um häufig gestellte Fragen (FAQs) zu beantworten.
3. **Webscraping**: Wenn keine passende Antwort in der Datenbank gefunden wird, durchsucht der Bot eine definierte Website, um relevante Informationen zu extrahieren.
4. **Fuzzy-Matching**: Dank `fuzzywuzzy` erkennt der Bot auch ähnliche Fragen und gibt die passende Antwort zurück.
5. **Sprachunterstützung**: Der Bot unterstützt sowohl Englisch als auch Deutsch und nutzt `deep_translator` zur automatischen Übersetzung.
6. **KI-Antworten**: Falls keine Antwort aus der Datenbank oder durch Webscraping gefunden wird, greift der Bot auf OpenAI (GPT) zurück.
7. **Memory-Funktion**: Der ChatBot speichert frühere Konversationen, um mit vergangenen Fragen über ChatGPT zu interagieren.
8. **Automatische Datenbereinigung**: Alte Konversationsdaten werden regelmäßig gelöscht, um die Datenbank aktuell und sauber zu halten.

---

# **Lücken und Verbesserungsbedarf**

Obwohl der ChatBot viele nützliche Funktionen bietet, gibt es noch Raum für Optimierungen:

1. **KI-Fallback**: 
   - Der KI-Fallback funktioniert nur, wenn ein OpenAI-API-Konto mit aktiviertem Billing eingerichtet ist. Nutzer müssen dies vorab tun.
   
2. **Fuzzy-Matching**:
   - Die Ähnlichkeitsgrenze ist derzeit auf 75 % festgelegt. Eine dynamische Anpassung könnte zu besseren Ergebnissen führen.
   
3. **Fehlerbehandlung bei APIs**:
   - Eine robustere Fehlerbehandlung für Übersetzungs- und KI-Anfragen wäre hilfreich.

4. **Datenbank**:
   - Die Datenbank ist momentan nur mit Beispiel-Daten gefüllt. Eine vollständige Datenbank mit relevanten FAQs ist geplant.
   
5. **Performance**:
   - Die aktuelle Datenbanklösung ist gut für kleine Datenmengen geeignet, muss aber bei größeren Volumina optimiert werden.

---

## **Anleitung zur Ausführung**

### Voraussetzungen

- **Python**: Version 3.9 oder höher
- **Abhängigkeiten**: Installiere die erforderlichen Python-Bibliotheken durch:
  ```bash
  pip install -r requirements.txt
  ```

### Schritte zur Ausführung

1. **Datenbank initialisieren**:
   Stelle sicher, dass die SQLite-Datenbank korrekt eingerichtet wird:
   ```bash
   python -c "from Backup import init_db; init_db()"
   ```

2. **Chatbot starten**:
   Führe das Hauptskript aus:
   ```bash
   python Backup.py
   ```

3. **Zugriff auf die Benutzeroberfläche**:
   Öffne deinen Browser und gehe zu:
   ```
   http://localhost:5001
   ```

4. **Integrationstest**:
   Sende POST-Anfragen an `/ask` mit JSON-Daten wie:
   ```json
   {
     "question": "Was sind die Vorteile eures Produkts?",
     "language": "de"
   }
   ```

---

## **Commit-Verlauf**

Der vollständige Verlauf der Änderungen ist im `commit_history.md` verfügbar.

---

## **Wichtige Hinweise**

- **Vertrauliche Daten**: Achte darauf, dass keine vertraulichen Informationen (z. B. API-Schlüssel) im Repository landen. Nutze Umgebungsvariablen oder sichere Konfigurationsdateien.
- **GitHub Secret Scanning**: Um zu verhindern, dass versehentlich vertrauliche Daten gepusht werden, sollte das Secret Scanning auf GitHub aktiviert werden. Gehe zu den Repository-Einstellungen und aktiviere unter "Security & analysis" die Option "Secret scanning".

---

Viel Spaß bei der Nutzung des ChatBots!
