import tkinter as tk
from tkinter import filedialog
from core.core import read_file, write_file, PluginManager, select_and_apply_plugins

def main():
    while True:  # Schleife, um das Tool bei Bedarf erneut auszuführen
        # Begrüßungsnachricht
        print("Welcome to the word processing program!")

        # Initialize Tkinter
        root = tk.Tk()
        root.withdraw()  # Versteckt das Hauptfenster

        # Datei auswählen für Input
        print("\nSelect the input file:")
        input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not input_file:
            print("No input file selected. Exiting...")
            return

        # Datei auswählen für Output
        print("\nSelect the output file (or specify a new file):")
        output_file = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not output_file:
            print("No output file selected. Exiting...")
            return

        # Eingabedatei lesen
        text = read_file(input_file)
        print("\nLoaded text:")
        print(text)

        # Plugins laden und anwenden
        plugin_manager = PluginManager()
        plugin_manager.load_plugins()
        processed_text = select_and_apply_plugins(text, plugin_manager.plugins)

        # Ergebnis speichern und anzeigen
        write_file(output_file, processed_text)
        print("\nOutput File Content:\n")
        print(read_file(output_file))

        # Benutzer fragen, ob das Tool erneut ausgeführt werden soll
        retry = input("\nDo you want to process another file? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Thank you for using the tool! Goodbye!")
            break  # Schleife verlassen, Programm beenden

if __name__ == "__main__":
    main()
