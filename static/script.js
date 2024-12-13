// Chatbot-Elemente
const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatInput = document.getElementById('chat-input');
const chatBotContainer = document.getElementById('chatbot-container');
const feedbackContainer = document.getElementById('feedback-container');
let selectedLanguage = null; // Aktuell ausgewählte Sprache


// Funktion: Nachricht in das Chatfenster einfügen
function appendMessage(content, sender) {
    const message = document.createElement('div');
    message.className = sender === 'bot' ? 'message-bot' : 'message-user';
    message.innerHTML = `<span>${content}</span>`;
    chatWindow.appendChild(message);
    message.scrollIntoView({ behavior: 'smooth' }); // Fließendes Scrollen
}

function resetStars() {
    const stars = document.querySelectorAll('.stars .star');
    stars.forEach(star => {
        star.classList.remove('selected'); // Entfernt die Klasse "selected"
        star.style.color = '#fff'; // Setzt die Farbe auf die Standardfarbe (z. B. Weiß)
    });
    selectedRating = 0; // Setzt das Feedback-Rating zurück
}

// Funktion: Antwort abrufen
function fetchAnswer(userMessage) {
    const response =
        botResponses[selectedLanguage]?.default ||
        (selectedLanguage === 'en'
            ? "Sorry, I don't have an answer for that."
            : "Entschuldigung, ich habe darauf keine Antwort.");
    appendMessage(response, 'bot'); // Chatbot-Antwort hinzufügen
}

// Event Listener für Senden-Button
sendButton.addEventListener('click', () => {
    const userMessage = userInput.value.trim();
    if (userMessage === '') return; // Leere Eingaben ignorieren
    if (!selectedLanguage) {
        appendMessage('Please select a language first.', 'bot');
        return;
    }
    appendMessage(userMessage, 'user'); // Benutzer-Nachricht hinzufügen
    userInput.value = '';
    fetchAnswer(userMessage);
});

// Funktion: Sprachwahlbuttons hinzufügen
function addLanguageButtons() {
    const languageButtons = document.createElement('div');
    languageButtons.className = 'language-buttons';
    languageButtons.innerHTML = `
        <button class="english" onclick="setLanguage('en')">English</button>
        <button class="german" onclick="setLanguage('de')">Deutsch</button>
    `;
    chatWindow.appendChild(languageButtons);
}

// Funktion: Sprache setzen
function setLanguage(language) {
    selectedLanguage = language;
    appendMessage(
        language === 'en'
            ? 'Great! You can now ask me anything in English.'
            : 'Super! Du kannst mir jetzt auf Deutsch Fragen stellen.',
        'bot'
    );
    document.querySelector('.language-buttons').remove();
    chatInput.style.display = 'flex'; // Chat-Input anzeigen
}

let selectedRating = 0;

function rateFeedback(rating) {
    selectedRating = rating;
    updateStarColors();
}

function updateStarColors() {
    const stars = document.querySelectorAll('.stars .star');
    stars.forEach((star, index) => {
        if (index < selectedRating) {
            star.classList.add('selected');
        } else {
            star.classList.remove('selected');
        }
    });
}

document.querySelectorAll('.stars .star').forEach((star, index) => {
    star.addEventListener('mouseover', () => {
        for (let i = 0; i <= index; i++) {
            document.querySelectorAll('.stars .star')[i].style.color = 'gold';
        }
    });

    star.addEventListener('mouseout', () => {
        document.querySelectorAll('.stars .star').forEach((s, i) => {
            s.style.color = i < selectedRating ? 'gold' : '';
        });
    });

    star.addEventListener('click', () => {
        rateFeedback(index + 1);
    });
});

// Event Listener für Enter-Taste
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendButton.click();
});



// Funktion: Chat starten
function startChat() {
    document.getElementById('nova-section').classList.add('hidden'); // Nova-Intro verstecken
    document.getElementById('chatbot-container').classList.remove('hidden'); // Chatbot anzeigen
}

// Funktion: Feedbackfenster öffnen
function openFeedback() {
    document.getElementById('chatbot-container').classList.add('hidden'); // Chatbot verstecken
    document.getElementById('feedback-container').classList.remove('hidden'); // Feedback-Fenster anzeigen
    resetStars(); // Sterne zurücksetzen
}

// Funktion: Zurück zum Chatbot
function backToChat() {
    document.getElementById('feedback-container').classList.add('hidden'); // Feedback-Fenster verstecken
    document.getElementById('chatbot-container').classList.remove('hidden'); // Chatbot anzeigen
    resetStars(); // Sterne zurücksetzen
}

// Event-Listener für den Feedback-Button
document.getElementById('feedback-button').addEventListener('click', openFeedback);

async function fetchAnswer(userMessage) {
    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userMessage, language: selectedLanguage }),
        });

        if (!response.ok) throw new Error('Server antwortet nicht');

        const data = await response.json();

        if (data && data.response && data.response.answer) {
            appendMessage(data.response.answer, 'bot');
        } else {
            appendMessage('Entschuldigung, es gab ein Problem mit der Antwort.', 'bot');
        }
    } catch (error) {
        appendMessage('Entschuldigung, es gab ein Problem mit dem Server.', 'bot');
    }
}

appendMessage('Hello! Would you like to chat in English or German?', 'bot');
addLanguageButtons();

sendButton.addEventListener('click', () => {
    const userMessage = userInput.value.trim();
    if (userMessage === '' || !selectedLanguage) return;
    appendMessage(userMessage, 'user');
    userInput.value = '';
    fetchAnswer(userMessage);
});

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendButton.click();
});