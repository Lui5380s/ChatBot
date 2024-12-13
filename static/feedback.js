document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.stars .star');
    const feedbackText = document.getElementById('feedback-text');
    let selectedRating = 0;

    // Sterne anklickbar machen
    stars.forEach(star => {
        // Hover-Effekt hinzufügen
        star.addEventListener('mouseover', () => {
            const hoverValue = parseInt(star.getAttribute('data-value'));
            stars.forEach(s => s.classList.toggle('highlight', s.getAttribute('data-value') <= hoverValue));
        });

        // Hover-Effekt entfernen
        star.addEventListener('mouseout', () => {
            stars.forEach(s => s.classList.remove('highlight'));
            if (selectedRating > 0) {
                stars.forEach(s => s.classList.toggle('selected', s.getAttribute('data-value') <= selectedRating));
            }
        });

        // Klick-Ereignis
        star.addEventListener('click', () => {
            selectedRating = parseInt(star.getAttribute('data-value'));
            stars.forEach(s => s.classList.toggle('selected', s.getAttribute('data-value') <= selectedRating));
            console.log(`Bewertung ausgewählt: ${selectedRating} Sterne`); // Debugging: Ausgabe der ausgewählten Sterne
        });
    });


    // Feedback absenden
    window.submitFeedback = () => {
        const feedbackValue = feedbackText.value.trim();

        if (selectedRating === 0) {
            alert('Bitte wählen Sie eine Bewertung aus.');
            return;
        }

        if (feedbackValue.length < 3) {
            alert('Ihr Feedback ist zu kurz. Bitte geben Sie mindestens 3 Zeichen ein.');
            return;
        }

        const feedbackData = {
            rating: selectedRating,
            feedbackText: feedbackValue
        };

        console.log('Feedback wird gesendet:', feedbackData); // Debugging: Feedback-Daten ausgeben

        // Daten an den Server senden
        fetch('/submit-feedback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(feedbackData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                console.log('Feedback erfolgreich gespeichert:', data); // Erfolgsnachricht in der Konsole
                alert(data.message); // Erfolgsnachricht für den Nutzer
                feedbackText.value = ''; // Feedback-Text zurücksetzen
                selectedRating = 0; // Bewertung zurücksetzen
                stars.forEach(s => s.classList.remove('selected')); // Sterne-Highlight zurücksetzen
            } else {
                console.error('Fehler beim Speichern des Feedbacks:', data.error);
                alert(data.error || 'Ein Fehler ist aufgetreten.');
            }
        })
        .catch(error => {
            console.error('Fehler beim Senden des Feedbacks:', error);
            alert('Es gab ein Problem beim Absenden Ihres Feedbacks.');
        });
    };
});