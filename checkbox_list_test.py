import tkinter as tk

def on_checkbox_selected():
    selected_items = [objects[i] for i, var in enumerate(checkbox_vars) if var.get() == 1]
    print("Wybrane elementy:", selected_items)

root = tk.Tk()
root.geometry("400x300")

# Tworzenie podziału na 30% i 70%
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=7)

# Tworzenie listy obiektów
objects = ["Obiekt 1", "Obiekt 2", "Obiekt 3", "Obiekt 4", "Obiekt 5"]

# Tworzenie zmiennych przechowujących stany checkboxów
checkbox_vars = []

# Tworzenie ramki dla listy obiektów
frame_objects = tk.Frame(root)
frame_objects.grid(row=0, column=0, sticky="nsew")

# Tworzenie paska przewijania dla listy obiektów
scrollbar = tk.Scrollbar(frame_objects)
scrollbar.pack(side="right", fill="y")

# Tworzenie Canvas dla listy obiektów
canvas = tk.Canvas(frame_objects, yscrollcommand=scrollbar.set)
canvas.pack(fill="both", expand=True)

# Dodawanie obiektów do Canvas
frame_listbox = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_listbox, anchor='nw')

# Dodawanie checkboxów do listy
for i, obj in enumerate(objects):
    var = tk.IntVar()
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(frame_listbox, text=obj, variable=var)
    checkbox.grid(row=i, column=0, sticky='w')

# Ustawianie rozmiaru Canvas
frame_listbox.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

scrollbar.config(command=canvas.yview)

# Tworzenie ramki dla drugiej części okna
frame_other = tk.Frame(root, bg="gray")
frame_other.grid(row=0, column=1, sticky="nsew")

# Przypisanie proporcji dla podziału
root.grid_rowconfigure(0, weight=1)

# Przypisanie proporcji dla listy obiektów
frame_objects.grid_rowconfigure(0, weight=1)
frame_objects.grid_columnconfigure(0, weight=1)

# Obsługa zdarzenia zaznaczenia checkboxa
for var in checkbox_vars:
    var.trace("w", lambda *args: on_checkbox_selected())

root.mainloop()
