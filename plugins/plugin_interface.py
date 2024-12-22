class PluginInterface:
    name = "Base Plugin"

    def process(self, text: str) -> str:
        raise NotImplementedError("Each plugin must implement the process method.")
