import tkinter as tk
from tkinter import ttk

class Concesionario:
    def __init__(self, root):
        self.root = root
        self.root.title("Concesionario de Motos")
        self.root.geometry("600x400")

        # --- Área del formulario ---
        self.form_frame = tk.LabelFrame(root, text="Datos de la Moto", padx=10, pady=10)
        self.form_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(self.form_frame, text="Marca:").grid(row=0, column=0, sticky="e")
        self.marca_entry = tk.Entry(self.form_frame)
        self.marca_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Modelo:").grid(row=0, column=2, sticky="e")
        self.modelo_entry = tk.Entry(self.form_frame)
        self.modelo_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.form_frame, text="Año:").grid(row=1, column=0, sticky="e")
        self.modelo_entry = tk.Entry(self.form_frame)
        self.modelo_entry.grid(row=1, column=1, padx=5, pady=5 )


        # --- Botones de acción ---
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill="x", padx=10, pady=5)

        self.agregar_btn = tk.Button(self.button_frame, text="Agregar Moto")
        self.agregar_btn.pack(side="left", padx=5)

        self.eliminar_btn = tk.Button(self.button_frame, text="Eliminar Seleccionada")
        self.eliminar_btn.pack(side="left", padx=5)

        # --- Tabla para mostrar motos ---
        self.tabla_frame = tk.LabelFrame(root, text="Inventario", padx=10, pady=10)
        self.tabla_frame.pack(fill="both", expand=True, padx=10, pady=5)

        columnas = ("Marca", "Modelo")
        self.tree = ttk.Treeview(self.tabla_frame, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True)

# --- Ejecutar ---
if __name__ == "__main__":
    root = tk.Tk()
    app = Concesionario(root)
    root.mainloop()
