from flask import Flask, request, jsonify, render_template
import sqlite3
import requests
import openai
from bs4 import BeautifulSoup
import re
import spacy
import numpy as np
from langdetect import detect
from deep_translator import GoogleTranslator
from fuzzywuzzy import fuzz, process
from nltk.tokenize import sent_tokenize, word_tokenize
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import nltk
import logging

# Punkt-Daten für NLTK
nltk.download('punkt')

# Logging konfigurieren
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Flask-App initialisieren
app = Flask(__name__)

# OpenAI-API-Schlüssel
openai.api_key = "sk-..."

# Lade das spaCy-Modell für Deutsch
nlp = spacy.load("de_core_news_md")

# Datenbank initialisieren
def init_db():
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT UNIQUE,
            answer TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    logging.info("Datenbank erfolgreich initialisiert.")

# Lade FAQ-Daten aus der Datenbank
def load_faq_data():
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM faq")
    rows = cursor.fetchall()
    faq_data = [{"question": row[0], "answer": row[1]} for row in rows]
    conn.close()
    logging.info("FAQ-Daten erfolgreich geladen.")
    return faq_data

# Alte Konversationen aus der Datenbank entfernen
def clean_old_conversations(days=1):
    threshold_date = datetime.now() - timedelta(days=days)
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM conversation_history
        WHERE timestamp < ?
    ''', (threshold_date,))
    conn.commit()
    conn.close()
    logging.info(f"Konversationen älter als {days} Tag(e) entfernt.")

# Scheduler starten
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(clean_old_conversations, 'interval', days=1, args=[7])  # Bereinige täglich
    scheduler.start()
    logging.info("Scheduler für das Löschen alter Konversationen gestartet.")

# Übersetzung ins Deutsche
def translate_to_german(text):
    try:
        return GoogleTranslator(source='auto', target='de').translate(text)
    except Exception as e:
        logging.error(f"Fehler bei der Übersetzung ins Deutsche: {e}")
        return text

# Übersetzung ins Englische
def translate_to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except Exception as e:
        logging.error(f"Fehler bei der Übersetzung ins Englische: {e}")
        return text

# Sprache erkennen
def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        logging.error(f"Fehler bei der Spracherkennung: {e}")
        return "unknown"

# Text normalisieren
def normalize_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Entfernt Satzzeichen
    return text.lower().strip()

# Fuzzy Matching für die beste Frage
def find_best_match(user_input, faq_data):
    questions = [item["question"] for item in faq_data]
    best_match, score = process.extractOne(user_input, questions, scorer=fuzz.ratio)
    if score >= 75:
        logging.info(f"Beste Übereinstimmung gefunden: {best_match} mit Punktzahl: {score}")
        return best_match
    logging.info("Keine ausreichende Übereinstimmung gefunden.")
    return None

# KI-Modell-Antwort generieren
def ai_model_answer(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=150,
            temperature=0.7
        )
        logging.info(f"Antwort vom KI-Modell: {response['choices'][0]['message']['content'].strip()}")
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error(f"Fehler bei der Anfrage an OpenAI: {e}")
        return "Entschuldigung, ich konnte keine Antwort finden."

# Scraping mit Wortbegrenzung (30 Wörter)
def scrape_website_for_answer(question):
    try:
        url = "https://www.innoai-solutions.com/"
        response = requests.get(url)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            logging.error(f"Fehler beim Abrufen der Website: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text().lower()
        keywords = re.findall(r'\b(vorteile|dienstleistungen|angebote?|lösungen?|produkte?|team|kontakt|adresse|faq|vision)\b', question.lower())
        matched_content = re.findall(r'([^.]*\b' + r'\b|\b'.join(map(re.escape, keywords)) + r'\b[^.]*\.)', content)

        if matched_content:
            full_text = " ".join(matched_content)
            sentences = sent_tokenize(full_text)
            selected_sentences = []
            word_count = 0

            for sentence in sentences:
                words = word_tokenize(sentence)
                word_count += len(words)
                selected_sentences.append(sentence)
                if word_count >= 30:
                    break

            result_text = " ".join(selected_sentences)
            result_words = word_tokenize(result_text)

            if len(result_words) > 30:
                result_text = " ".join(result_words[:30])

            return {
                "topic": "Webscraping",
                "explanation": result_text
            }

        return None
    except Exception as e:
        logging.error(f"Fehler beim Scraping: {e}")
        return None

@app.route('/')
def index():
    logging.info("Benutzer greift auf die Hauptseite zu.")
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get('question')
    selected_language = data.get('language')

    if not user_input or not selected_language:
        logging.error("Frage oder Sprache fehlt.")
        return jsonify({"error": "Frage oder Sprache fehlt"}), 400

    is_english = selected_language == 'en'
    german_input = translate_to_german(user_input) if is_english else user_input
    normalized_input = normalize_text(german_input)
    faq_data = load_faq_data()
    best_match_question = find_best_match(normalized_input, faq_data)

    answer = None
    if best_match_question:
        for item in faq_data:
            if item["question"] == best_match_question:
                answer = item["answer"]
                break

    if not answer:
        scraped_data = scrape_website_for_answer(normalized_input)
        if scraped_data:
            topic = scraped_data.get("topic", "Relevante Informationen")
            explanation = scraped_data.get("explanation", "Hier sind die Details:")
            answer = f"{topic}: {explanation}"
        else:
            answer = ai_model_answer(normalized_input)

    if is_english:
        answer = translate_to_english(answer)

    # Speichere die Unterhaltung in der Datenbank
    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO conversation_history (user_input, bot_response)
        VALUES (?, ?)
    ''', (user_input, answer))
    conn.commit()
    conn.close()
    logging.info(f"Antwort gespeichert: {user_input} -> {answer}")

    return jsonify({"response": {"question": user_input, "answer": answer}})

if __name__ == "__main__":
    init_db()
    start_scheduler()
    app.run(host='0.0.0.0', port=5001, debug=True)
    