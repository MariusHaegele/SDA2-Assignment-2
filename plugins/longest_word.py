from plugins.plugin_interface import PluginInterface

class Plugin(PluginInterface):
    name = "Longest Word Finder"

    def process(self, text: str) -> str:
        # Text in Wörter aufteilen und Sonderzeichen entfernen
        words = [word.strip('.,!?;:"()[]') for word in text.split()]
        
        # Längstes Wort finden
        longest_word = max(words, key=len)
        length = len(longest_word)
        
        # Ergebnis formatieren
        result = f"Longest Word: {longest_word}\nLength: {length}"
        return result
