from plugins.plugin_interface import PluginInterface
from collections import Counter

class Plugin(PluginInterface):
    name = "Word Frequency"

    def process(self, text: str) -> str:
        # Wörter bereinigen und in Kleinbuchstaben umwandeln
        words = [word.strip('.,!?').lower() for word in text.split()]
        
        # Wortanzahl ermitteln
        word_counts = Counter(words)
        
        # Top 10 häufigste Wörter finden
        most_common = word_counts.most_common(10)
        
        # Histogramm erstellen (ohne Titel)
        result = ""
        for word, count in most_common:
            result += f"{word}: {'*' * count}\n"
        
        return result
