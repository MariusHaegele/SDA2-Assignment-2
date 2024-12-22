from plugins.plugin_interface import PluginInterface

class Plugin(PluginInterface):
    name = "Case Converter"

    def process(self, text: str) -> str:
        print("\n1. Uppercase\n2. Lowercase\n3. Capitalized")
        choice = int(input("Select an option: "))
        if choice == 1:
            return text.upper()
        elif choice == 2:
            return text.lower()
        elif choice == 3:
            return text.title()
        return text
