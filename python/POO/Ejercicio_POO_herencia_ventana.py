import tkinter as tk

class VentanaBase:
    def __init__(self, titulo) -> None:
        self.ventana = tk.Tk()
        self.ventana.title(titulo)
        self.ventana.geometry("300x200")
    def mostrar(self):
        self.ventana.mainloop()

class VentanaSaludo(VentanaBase):
    def __init__(self) -> None:
        super().__init__("Ventana de saludo")
        etiqueta = tk.Label(self.ventana, text="Hola mundo")
        etiqueta.pack(pady=50)

        boton = tk.Button(self.ventana, text="cerrar", command=self.ventana.destroy)
        boton.pack()

app = VentanaSaludo()
app.mostrar()