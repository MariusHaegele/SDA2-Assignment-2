from plugins.plugin_interface import PluginInterface

class Plugin(PluginInterface):
    name = "Word Counter"

    def process(self, text: str) -> str:
        word_count = len(text.split())
        return f"Word Count: {word_count}"
