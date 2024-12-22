import importlib
import os

class PluginManager:
    """
    Manages the dynamic loading and handling of plugins.
    """
    def __init__(self, plugin_folder='plugins'):
        self.plugins = []
        self.plugin_folder = plugin_folder

    def load_plugins(self):
        """
        Dynamically loads all plugins from the specified folder.
        """
        for file in os.listdir(self.plugin_folder):
            if file.endswith('.py') and file != '__init__.py':
                module_name = f"{self.plugin_folder}.{file[:-3]}"
                module = importlib.import_module(module_name)
                if hasattr(module, 'Plugin'):  # Check if the module has a 'Plugin' class
                    self.plugins.append(module.Plugin())


def read_file(file_path):
    """
    Reads text from a file.
    :param file_path: Path to the input file.
    :return: Text content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, content):
    """
    Writes text to a file.
    :param file_path: Path to the output file.
    :param content: Text content to write.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def select_and_apply_plugins(text, plugins):
    """
    Allows the user to select and apply multiple plugins to the text sequentially.
    :param text: The input text to process.
    :param plugins: List of available plugins.
    :return: Combined results of all selected plugins.
    """
    print("\nAvailable Plugins:")
    for i, plugin in enumerate(plugins):
        print(f"{i + 1}. {plugin.name}")
    
    selected_plugins = input("\nSelect plugins by numbers separated by commas (e.g., 1,3): ")
    selected_indices = [int(x.strip()) - 1 for x in selected_plugins.split(",") if x.strip().isdigit()]

    results = []  # List to store results from all plugins

    for index in selected_indices:
        if 0 <= index < len(plugins):
            print(f"\nApplying plugin: {plugins[index].name}")
            processed_text = plugins[index].process(text)
            results.append(f"{plugins[index].name}:\n{processed_text}\n")
        else:
            print(f"Invalid choice: {index + 1}")

    return "\n".join(results)  # Combine results from all plugins
