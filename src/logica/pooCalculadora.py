# src/gui_app.py

import tkinter as tk
from tkinter import messagebox
from src.logica.calculadora import CalculadoraEstadistica, NoSePuedeCalcular


class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Media y Desviación Estándar")

        # Instancia de la clase CalculadoraEstadistica
        self.calculadora = CalculadoraEstadistica()

        # Crear elementos de la interfaz
        self.label = tk.Label(root, text="Ingresa un número:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.agregar_btn = tk.Button(root, text="Agregar número", command=self.agregar_numero)
        self.agregar_btn.pack()

        self.calcular_media_btn = tk.Button(root, text="Calcular Media", command=self.mostrar_media)
        self.calcular_media_btn.pack()

        self.calcular_desviacion_btn = tk.Button(root, text="Calcular Desviación Estándar",
                                                 command=self.mostrar_desviacion_estandar)
        self.calcular_desviacion_btn.pack()

        self.limpiar_btn = tk.Button(root, text="Limpiar elementos", command=self.limpiar_elementos)
        self.limpiar_btn.pack()

        self.lista_label = tk.Label(root, text="Elementos ingresados:")
        self.lista_label.pack()

        self.lista_elementos = tk.Listbox(root)
        self.lista_elementos.pack()

    def agregar_numero(self):
        try:
            numero = float(self.entry.get())
            self.calculadora.agregar_elemento(numero)
            self.lista_elementos.insert(tk.END, numero)
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        except TypeError as e:
            messagebox.showerror("Error", str(e))

    def mostrar_media(self):
        try:
            media = self.calculadora.calcular_media()
            messagebox.showinfo("Resultado", f"La media es: {media}")
        except NoSePuedeCalcular as e:
            messagebox.showerror("Error", str(e))

    def mostrar_desviacion_estandar(self):
        try:
            desviacion_estandar = self.calculadora.calcular_desviacion_estandar()
            messagebox.showinfo("Resultado", f"La desviación estándar es: {desviacion_estandar}")
        except NoSePuedeCalcular as e:
            messagebox.showerror("Error", str(e))

    def limpiar_elementos(self):
        self.calculadora.limpiar_elementos()
        self.lista_elementos.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
