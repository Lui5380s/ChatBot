import sqlite3
import os

# Absoluter oder relativer Pfad zur bestehenden Datenbank im 'Test'-Ordner
db_path = os.path.join("Test", "FAQ.db")

# Verbindung zur bestehenden Datenbank herstellen
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tabelle erstellen, falls sie noch nicht existiert
cursor.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
""")

# Fragen und Antworten einfügen
faqs = [
    # Abschnitt 1
    ("Was ist InnoAI Solutions?", "InnoAI Solutions ist ein Anbieter für digitale B2B-Dienstleistungen. Wir helfen Unternehmen, ihre Arbeitsprozesse durch den Einsatz von künstlicher Intelligenz effizienter zu gestalten. Unser Ziel ist es, wiederkehrende Aufgaben zu automatisieren und Zeit für wichtigere Tätigkeiten freizusetzen."),
    ("Wer oder was ist InnoAI Solutions?", "InnoAI Solutions ist ein Anbieter für digitale B2B-Dienstleistungen. Wir helfen Unternehmen, ihre Arbeitsprozesse durch den Einsatz von künstlicher Intelligenz effizienter zu gestalten. Unser Ziel ist es, wiederkehrende Aufgaben zu automatisieren und Zeit für wichtigere Tätigkeiten freizusetzen."),
    ("Können Sie mir mehr über Ihr Unternehmen erzählen?", "InnoAI Solutions ist ein Anbieter für digitale B2B-Dienstleistungen. Wir helfen Unternehmen, ihre Arbeitsprozesse durch den Einsatz von künstlicher Intelligenz effizienter zu gestalten. Unser Ziel ist es, wiederkehrende Aufgaben zu automatisieren und Zeit für wichtigere Tätigkeiten freizusetzen."),
    ("Was genau macht InnoAI Solutions?", "InnoAI Solutions ist ein Anbieter für digitale B2B-Dienstleistungen. Wir helfen Unternehmen, ihre Arbeitsprozesse durch den Einsatz von künstlicher Intelligenz effizienter zu gestalten. Unser Ziel ist es, wiederkehrende Aufgaben zu automatisieren und Zeit für wichtigere Tätigkeiten freizusetzen."),
    # Abschnitt 2
    ("Was macht InnoAI Solutions besonders?", "Wir setzen auf maßgeschneiderte KI-Lösungen, die einfach zu nutzen und schnell implementierbar sind. Unser Fokus liegt darauf, Prozesse zu optimieren, ohne die Expertise Ihres Teams zu ersetzen."),
    ("Warum sollte ich mich für InnoAI Solutions entscheiden?", "Wir setzen auf maßgeschneiderte KI-Lösungen, die einfach zu nutzen und schnell implementierbar sind. Unser Fokus liegt darauf, Prozesse zu optimieren, ohne die Expertise Ihres Teams zu ersetzen."),
    ("Was unterscheidet Sie von anderen Anbietern?", "Wir setzen auf maßgeschneiderte KI-Lösungen, die einfach zu nutzen und schnell implementierbar sind. Unser Fokus liegt darauf, Prozesse zu optimieren, ohne die Expertise Ihres Teams zu ersetzen."),
    ("Was ist das Besondere an Ihren Lösungen?", "Wir setzen auf maßgeschneiderte KI-Lösungen, die einfach zu nutzen und schnell implementierbar sind. Unser Fokus liegt darauf, Prozesse zu optimieren, ohne die Expertise Ihres Teams zu ersetzen."),
    # Abschnitt 3
    ("Welche Dienstleistungen bieten Sie an?", "Wir bieten: ChatGPT-gestützte Chatbots zur Automatisierung von Kundenanfragen, automatisierte Inserat-Erstellung für Autohäuser und andere Branchen, Lead-Management-Systeme zur Erfassung und Nachverfolgung von Interessenten, personalisierte Marketingkampagnen und E-Mail-Automatisierung, sowie Schulungsvideos zur eigenständigen Nutzung unserer KI-Tools."),
    ("Was kann ich von Ihren Services erwarten?", "Wir bieten: ChatGPT-gestützte Chatbots zur Automatisierung von Kundenanfragen, automatisierte Inserat-Erstellung für Autohäuser und andere Branchen, Lead-Management-Systeme zur Erfassung und Nachverfolgung von Interessenten, personalisierte Marketingkampagnen und E-Mail-Automatisierung, sowie Schulungsvideos zur eigenständigen Nutzung unserer KI-Tools."),
   ("Welche Lösungen haben Sie im Angebot?", "Wir bieten: ChatGPT-gestützte Chatbots zur Automatisierung von Kundenanfragen, automatisierte Inserat-Erstellung für Autohäuser und andere Branchen, Lead-Management-Systeme zur Erfassung und Nachverfolgung von Interessenten, personalisierte Marketingkampagnen und E-Mail-Automatisierung, sowie Schulungsvideos zur eigenständigen Nutzung unserer KI-Tools."),
    # Abschnitt 4
    ("Wie helfen Ihre Lösungen meinem Unternehmen?", "Unsere KI-gestützten Tools automatisieren wiederkehrende Aufgaben, sparen Zeit und verbessern die Kundenkommunikation. Das Ergebnis: Mehr Effizienz, weniger manuelle Arbeit und eine gesteigerte Kundenzufriedenheit."),
    ("Wie verbessern Ihre Tools meine Abläufe?", "Unsere KI-gestützten Tools automatisieren wiederkehrende Aufgaben, sparen Zeit und verbessern die Kundenkommunikation. Das Ergebnis: Mehr Effizienz, weniger manuelle Arbeit und eine gesteigerte Kundenzufriedenheit."),
    ("Welche Vorteile bringen Ihre Services?", "Unsere KI-gestützten Tools automatisieren wiederkehrende Aufgaben, sparen Zeit und verbessern die Kundenkommunikation. Das Ergebnis: Mehr Effizienz, weniger manuelle Arbeit und eine gesteigerte Kundenzufriedenheit."),
    ("Wie kann mein Unternehmen von Ihnen profitieren?", "Unsere KI-gestützten Tools automatisieren wiederkehrende Aufgaben, sparen Zeit und verbessern die Kundenkommunikation. Das Ergebnis: Mehr Effizienz, weniger manuelle Arbeit und eine gesteigerte Kundenzufriedenheit."),
    ("Sind Ihre Lösungen nur für Autohäuser geeignet?", "Nein, unsere Lösungen sind flexibel und können auf verschiedene Branchen angepasst werden. Wir starten mit Autohäusern, planen aber, unsere Dienstleistungen auf weitere Branchen auszudehnen."),
    ("Arbeiten Sie ausschließlich mit Autohäusern?", "Nein, unsere Lösungen sind flexibel und können auf verschiedene Branchen angepasst werden. Wir starten mit Autohäusern, planen aber, unsere Dienstleistungen auf weitere Branchen auszudehnen."),
    ("Sind Ihre Services auch für andere Branchen nutzbar?", "Nein, unsere Lösungen sind flexibel und können auf verschiedene Branchen angepasst werden. Wir starten mit Autohäusern, planen aber, unsere Dienstleistungen auf weitere Branchen auszudehnen."),
    ("Kann ich Ihre Tools auch nutzen, wenn ich kein Autohaus betreibe?", "Nein, unsere Lösungen sind flexibel und können auf verschiedene Branchen angepasst werden. Wir starten mit Autohäusern, planen aber, unsere Dienstleistungen auf weitere Branchen auszudehnen."),
    # Abschnitt 5
    ("Was kann der Chatbot für mein Unternehmen tun?", "Unser Chatbot beantwortet häufige Kundenfragen, plant Probefahrten oder Termine, sammelt Kundeninformationen und entlastet Ihr Team bei der Bearbeitung von Standardanfragen – rund um die Uhr."),
    ("Wie könnte ein Chatbot in meinem Unternehmen eingesetzt werden?", "Unser Chatbot beantwortet häufige Kundenfragen, plant Probefahrten oder Termine, sammelt Kundeninformationen und entlastet Ihr Team bei der Bearbeitung von Standardanfragen – rund um die Uhr."),
    ("Was sind die Hauptfunktionen Ihres Chatbots?", "Unser Chatbot beantwortet häufige Kundenfragen, plant Probefahrten oder Termine, sammelt Kundeninformationen und entlastet Ihr Team bei der Bearbeitung von Standardanfragen – rund um die Uhr."),
    ("Welche Vorteile bietet Ihr Chatbot meinem Betrieb?", "Unser Chatbot beantwortet häufige Kundenfragen, plant Probefahrten oder Termine, sammelt Kundeninformationen und entlastet Ihr Team bei der Bearbeitung von Standardanfragen – rund um die Uhr."),
    ("Kann ich den Chatbot anpassen?", "Ja, unser Chatbot wird auf Ihre spezifischen Bedürfnisse und häufigen Anfragen angepasst, sodass er perfekt zu Ihrem Unternehmen passt."),
    ("Kann der Chatbot auf meine Bedürfnisse zugeschnitten werden?", "Ja, unser Chatbot wird auf Ihre spezifischen Bedürfnisse und häufigen Anfragen angepasst, sodass er perfekt zu Ihrem Unternehmen passt."),
    ("Kann ich den Bot mit eigenen Funktionen erweitern?", "Ja, unser Chatbot wird auf Ihre spezifischen Bedürfnisse und häufigen Anfragen angepasst, sodass er perfekt zu Ihrem Unternehmen passt."),
    ("Ist der Chatbot individuell konfigurierbar?", "Ja, unser Chatbot wird auf Ihre spezifischen Bedürfnisse und häufigen Anfragen angepasst, sodass er perfekt zu Ihrem Unternehmen passt."),
    # Abschnitt 6
    ("Was kosten Ihre Dienstleistungen?", "Unsere Dienstleistungen starten bei 500 EUR für das Basis-Paket und reichen bis zu 1.500 EUR monatlich für das Premium-Paket. Jedes Paket ist auf die Bedürfnisse Ihres Unternehmens abgestimmt. Weitere Details zu den Preisen finden Sie in unserem Angebot."),
    ("Wie hoch sind die Kosten für Ihre Lösungen?", "Unsere Dienstleistungen starten bei 500 EUR für das Basis-Paket und reichen bis zu 1.500 EUR monatlich für das Premium-Paket. Jedes Paket ist auf die Bedürfnisse Ihres Unternehmens abgestimmt. Weitere Details zu den Preisen finden Sie in unserem Angebot."),
    ("Welche Preismodelle bieten Sie an?", "Unsere Dienstleistungen starten bei 500 EUR für das Basis-Paket und reichen bis zu 1.500 EUR monatlich für das Premium-Paket. Jedes Paket ist auf die Bedürfnisse Ihres Unternehmens abgestimmt. Weitere Details zu den Preisen finden Sie in unserem Angebot."),
    ("Was muss ich für Ihre Services zahlen?", "Unsere Dienstleistungen starten bei 500 EUR für das Basis-Paket und reichen bis zu 1.500 EUR monatlich für das Premium-Paket. Jedes Paket ist auf die Bedürfnisse Ihres Unternehmens abgestimmt. Weitere Details zu den Preisen finden Sie in unserem Angebot."),
    # Abschnitt 7
    ("Gibt es eine Testversion?", "Ja, wir bieten eine kostenlose Demonstration unserer Lösungen an, damit Sie den Nutzen unserer Dienstleistungen vorab kennenlernen können."),
    ("Kann ich Ihre Dienste vor dem Kauf ausprobieren?", "Ja, wir bieten eine kostenlose Demonstration unserer Lösungen an, damit Sie den Nutzen unserer Dienstleistungen vorab kennenlernen können."),
    ("Bieten Sie eine kostenlose Demo an?", "Ja, wir bieten eine kostenlose Demonstration unserer Lösungen an, damit Sie den Nutzen unserer Dienstleistungen vorab kennenlernen können."),
    ("Kann ich Ihre Tools testen, bevor ich sie kaufe?", "Ja, wir bieten eine kostenlose Demonstration unserer Lösungen an, damit Sie den Nutzen unserer Dienstleistungen vorab kennenlernen können."),
    # Abschnitt 8
    ("Wie lange dauert die Implementierung?", "Die Implementierung unserer Lösungen dauert in der Regel zwischen 1 und 2 Wochen, abhängig von der Komplexität Ihrer Anforderungen."),
    ("Wie schnell kann ich Ihre Lösungen nutzen?", "Die Implementierung unserer Lösungen dauert in der Regel zwischen 1 und 2 Wochen, abhängig von der Komplexität Ihrer Anforderungen."),
    ("Dauert es lange, bis Ihre Tools einsatzbereit sind?", "Die Implementierung unserer Lösungen dauert in der Regel zwischen 1 und 2 Wochen, abhängig von der Komplexität Ihrer Anforderungen."),
    ("Wie läuft die Einrichtung Ihrer Systeme ab?", "Die Implementierung unserer Lösungen dauert in der Regel zwischen 1 und 2 Wochen, abhängig von der Komplexität Ihrer Anforderungen."),
    # Abschnitt 9
    ("Bieten Sie Support an?", "Ja, wir bieten monatlichen Support und regelmäßige Updates an, um sicherzustellen, dass Ihre Lösungen immer optimal funktionieren."),
    ("Unterstützen Sie uns auch nach der Einrichtung?", "Ja, wir bieten monatlichen Support und regelmäßige Updates an, um sicherzustellen, dass Ihre Lösungen immer optimal funktionieren."),
    ("Gibt es regelmäßigen Service oder Updates?", "Ja, wir bieten monatlichen Support und regelmäßige Updates an, um sicherzustellen, dass Ihre Lösungen immer optimal funktionieren."),
    ("Was passiert, wenn ich Probleme mit den Tools habe?", "Ja, wir bieten monatlichen Support und regelmäßige Updates an, um sicherzustellen, dass Ihre Lösungen immer optimal funktionieren."),
]

# Fragen in Kleinbuchstaben umwandeln, Antworten bleiben unverändert
faqs_lowercase_questions = [(question.lower(), answer) for question, answer in faqs]

# Daten in die Datenbank einfügen
cursor.executemany("INSERT INTO faq (question, answer) VALUES (?, ?)", faqs_lowercase_questions)

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Alle FAQs wurden erfolgreich in die Datenbank eingefügt (nur die Fragen in Kleinbuchstaben).")