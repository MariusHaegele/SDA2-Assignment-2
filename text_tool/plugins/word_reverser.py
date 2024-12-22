from plugins.plugin_interface import PluginInterface

class Plugin(PluginInterface):
    name = "Word Reverser"

    def process(self, text: str) -> str:
        reversed_words = ' '.join(word[::-1] for word in text.split())
        return reversed_words
