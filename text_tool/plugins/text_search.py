from plugins.plugin_interface import PluginInterface

class Plugin(PluginInterface):
    name = "Text Search"

    def process(self, text: str) -> str:
        query = input("Enter the word or phrase to search for: ")
        count = text.lower().count(query.lower())
        return f"'{query}' found {count} times."
