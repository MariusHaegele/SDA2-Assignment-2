from plugins.plugin_interface import PluginInterface

class Plugin(PluginInterface):
    name = "Character Counter"

    def process(self, text: str) -> str:
        total_characters = len(text)
        characters_without_spaces = len(text.replace(" ", ""))
        return (f"Total Characters: {total_characters}\n"
                f"Characters Without Spaces: {characters_without_spaces}")
