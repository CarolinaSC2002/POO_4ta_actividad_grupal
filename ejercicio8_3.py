import tkinter as tk
from tkinter import messagebox
import math

# --- Clases de Figuras Geométricas ---

class FiguraGeometrica:
    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    def set_volumen(self, volumen):
        self._volumen = volumen

    def set_superficie(self, superficie):
        self._superficie = superficie

    def get_volumen(self):
        return self._volumen

    def get_superficie(self):
        return self._superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        volumen = math.pi * self.altura * math.pow(self.radio, 2.0)
        return volumen

    def calcular_superficie(self):
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * math.pi * math.pow(self.radio, 2.0)
        return area_lado_a + area_lado_b

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        volumen = (4.0/3.0) * math.pi * math.pow(self.radio, 3.0)
        return volumen

    def calcular_superficie(self):
        superficie = 4.0 * math.pi * math.pow(self.radio, 2.0)
        return superficie

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        volumen = (math.pow(self.base, 2.0) * self.altura) / 3.0
        return volumen

    def calcular_superficie(self):
        area_base = math.pow(self.base, 2.0)
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado

# --- Clases de Ventanas Tkinter ---

class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        self.transient(master) # Hace que la ventana hija aparezca encima de la principal
        self.grab_set() # Bloquea la interacción con la ventana principal hasta que esta se cierre

        self.inicio()

    def inicio(self):
        # Ajustamos el ancho de las etiquetas y la posición de los campos de entrada
        self.radio_label = tk.Label(self, text="Radio (cms):")
        self.radio_label.place(x=20, y=20, width=80, height=23) # Ancho reducido para dar espacio
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=110, y=20, width=135, height=23) # Ajustado x

        self.altura_label = tk.Label(self, text="Altura (cms):")
        self.altura_label.place(x=20, y=50, width=80, height=23) # Ancho reducido
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=110, y=50, width=135, height=23) # Ajustado x

        self.calcular_button = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.place(x=100, y=80, width=135, height=23)

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=110, width=135, height=23)
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=140, width=135, height=23)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            
            cilindro = Cilindro(radio, altura)
            
            self.volumen_label.config(text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()

        self.inicio()

    def inicio(self):
        # Ajustamos el ancho de la etiqueta y la posición del campo de entrada
        self.radio_label = tk.Label(self, text="Radio (cms):")
        self.radio_label.place(x=20, y=20, width=80, height=23) # Ancho reducido
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=110, y=20, width=135, height=23) # Ajustado x

        self.calcular_button = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.place(x=100, y=50, width=135, height=23)

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=90, width=135, height=23)
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=120, width=135, height=23)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            
            esfera = Esfera(radio)
            
            self.volumen_label.config(text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()

        self.inicio()

    def inicio(self):
        # Ajustamos el ancho de las etiquetas y la posición de los campos de entrada
        self.base_label = tk.Label(self, text="Base (cms):")
        self.base_label.place(x=20, y=20, width=90, height=23) # Ancho ajustado
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=20, width=135, height=23)

        self.altura_label = tk.Label(self, text="Altura (cms):")
        self.altura_label.place(x=20, y=50, width=90, height=23) # Ancho ajustado
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50, width=135, height=23)

        self.apotema_label = tk.Label(self, text="Apotema (cms):")
        self.apotema_label.place(x=20, y=80, width=90, height=23) # Ancho ajustado
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=80, width=135, height=23)

        self.calcular_button = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.place(x=120, y=110, width=135, height=23)

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=140, width=135, height=23)
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=170, width=135, height=23)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            
            piramide = Piramide(base, altura, apotema)
            
            self.volumen_label.config(text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.inicio()

    def inicio(self):
        self.cilindro_button = tk.Button(self, text="Cilindro", command=self.mostrar_ventana_cilindro)
        self.cilindro_button.place(x=20, y=50, width=80, height=23)

        self.esfera_button = tk.Button(self, text="Esfera", command=self.mostrar_ventana_esfera)
        self.esfera_button.place(x=125, y=50, width=80, height=23)

        self.piramide_button = tk.Button(self, text="Pirámide", command=self.mostrar_ventana_piramide)
        self.piramide_button.place(x=225, y=50, width=100, height=23)

    def mostrar_ventana_cilindro(self):
        VentanaCilindro(self)

    def mostrar_ventana_esfera(self):
        VentanaEsfera(self)

    def mostrar_ventana_piramide(self):
        VentanaPiramide(self)

    def on_closing(self):
        self.destroy()

# --- Punto de entrada de la aplicación ---

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()