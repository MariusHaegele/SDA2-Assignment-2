from plugins.plugin_interface import PluginInterface
import re

class Plugin(PluginInterface):
    name = "Readability Checker"

    def process(self, text: str) -> str:
        # Anzahl der Sätze ermitteln
        sentences = re.split(r'[.!?]', text)
        sentences = [sentence for sentence in sentences if sentence.strip()]  # Leere Sätze entfernen
        num_sentences = len(sentences)

        # Anzahl der Wörter ermitteln
        words = text.split()
        num_words = len(words)

        # Anzahl der Silben ermitteln
        vowels = "aeiouy"
        num_syllables = 0
        for word in words:
            word = word.lower()
            word = re.sub(r'[^a-z]', '', word)  # Nur Buchstaben behalten
            syllable_count = 0
            previous_char_is_vowel = False
            for char in word:
                if char in vowels:
                    if not previous_char_is_vowel:
                        syllable_count += 1
                    previous_char_is_vowel = True
                else:
                    previous_char_is_vowel = False
            if word.endswith('e'):  # Stilles 'e' am Ende ignorieren
                syllable_count -= 1
            num_syllables += max(1, syllable_count)  # Mindestens 1 Silbe pro Wort

        # Flesch-Kincaid-Index berechnen
        if num_sentences > 0 and num_words > 0:
            flesch_score = 206.835 - (1.015 * (num_words / num_sentences)) - (84.6 * (num_syllables / num_words))
        else:
            flesch_score = 0  # Default-Wert für leere Texte

        # Bewertung basierend auf dem Flesch-Score
        if flesch_score >= 90:
            readability = "Very Easy"
        elif flesch_score >= 80:
            readability = "Easy"
        elif flesch_score >= 70:
            readability = "Fairly Easy"
        elif flesch_score >= 60:
            readability = "Standard"
        elif flesch_score >= 50:
            readability = "Fairly Difficult"
        elif flesch_score >= 30:
            readability = "Difficult"
        else:
            readability = "Very Confusing"

        # Ergebnis formatieren
        result = f"Readability Score (Flesch): {flesch_score:.2f}\nReadability Level: {readability}"
        return result
