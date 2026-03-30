import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.servicio = TareaServicio()

        self.crear_widgets()
        self.bind_eventos()

    def crear_widgets(self):
        self.entry_tarea = tk.Entry(self.root)
        self.entry_tarea.pack(pady=10, padx=10, fill="x")

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=5)

        self.btn_agregar = tk.Button(
            frame_botones, text="Añadir Tarea", command=self.agregar_tarea
        )
        self.btn_agregar.pack(side="left", padx=5)

        self.btn_completar = tk.Button(
            frame_botones, text="Marcar Completada", command=self.marcar_completada
        )
        self.btn_completar.pack(side="left", padx=5)

        self.btn_eliminar = tk.Button(
            frame_botones, text="Eliminar", command=self.eliminar_tarea
        )
        self.btn_eliminar.pack(side="left", padx=5)

        self.lista = tk.Listbox(self.root)
        self.lista.pack(fill="both", expand=True, padx=10, pady=10)

    # ================== EVENTOS ==================

    def bind_eventos(self):
        self.entry_tarea.bind("<Return>", lambda event: self.agregar_tarea())
        self.lista.bind("<Double-1>", lambda event: self.marcar_completada())

    # ================== ACCIONES ==================

    def agregar_tarea(self):
        descripcion = self.entry_tarea.get().strip()
        if descripcion:
            tarea = self.servicio.agregar_tarea(descripcion)
            self.lista.insert("end", f"{tarea.id}. {tarea.descripcion}")
            self.entry_tarea.delete(0, "end")

    def marcar_completada(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            texto = self.lista.get(index)
            id_tarea = int(texto.split(".")[0])

            self.servicio.marcar_completada(id_tarea)

            self.lista.delete(index)
            self.lista.insert(
                index, f"{id_tarea}. [Hecho] {texto.split('. ', 1)[1]}"
            )
            self.lista.itemconfig(index, fg="gray")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            texto = self.lista.get(index)
            id_tarea = int(texto.split(".")[0])

            self.servicio.eliminar_tarea(id_tarea)
            self.lista.delete(index)