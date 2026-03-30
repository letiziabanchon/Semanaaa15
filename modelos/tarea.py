class Tarea:
    def __init__(self, id_tarea, descripcion):
        self.id = id_tarea
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True