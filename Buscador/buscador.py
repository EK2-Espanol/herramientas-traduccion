import os
import tkinter as tk
from tkinter import messagebox


def search_word(entry):
    found_files_name = "resultados.txt"
    found_files = []
    found_lines = {}
    strings_to_search = entry.get().lower().split(",")
    for subdir, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".yml"):
                file_already_found = False
                file_path = os.path.join(subdir, file)
                with open(file_path, "r", encoding="utf-8-sig") as f:
                    lines = f.readlines()
                    for line_number, line in enumerate(lines):
                        if any(string.lower() in line.lower() for string in strings_to_search):
                            if not file_already_found: 
                                found_files.append(os.path.relpath(file_path))
                                file_already_found = True
                            if os.path.relpath(file_path) not in found_lines:
                                found_lines[os.path.relpath(file_path)] = []
                            found_lines[os.path.relpath(file_path)].append("Line {}: {}".format(line_number+1, line.strip()))


    if len(found_files) == 0:
        messagebox.showwarning("Advertencia","No se ha encontrado ninguna de las palabras introducidas.")
        return

    with open(found_files_name, "w", encoding="utf-8-sig") as found_files_txt:
        found_files_txt.write("Palabras buscadas: {}\n\n".format(", ".join(strings_to_search)))

        for file in found_files:
            found_files_txt.write("{}:\n".format(file))
            for line in found_lines[file]:
                found_files_txt.write("\t{}\n".format(line))

        os.startfile(found_files_name)

        found_files_txt.close()
        
            
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Buscador")
        self.geometry("500x200")
        self.resizable(0,0)

        self.label_entry = tk.Label(self, text="Introduce las palabras a buscar separadas por comas:")
        self.label_entry.pack(side='top')

        self.label_example = tk.Label(self, text="Ejemplo: escarcha, carrera blanca, pantano de las sombras")
        self.label_example.pack(side='top')

        self.entry = tk.Entry(self, width=60)
        self.entry.pack(side='top')

        self.search_button = tk.Button(self, width=10, text="Buscar", command=lambda: search_word(self.entry))
        self.search_button.pack(side='top')

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()