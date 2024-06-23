# -*- coding: utf-8 -*-

import tkinter as tk


def calcular_propina():
    try:
        monto_cuenta = float(monto_entry.get())
        porcentaje_propina = float(porcentaje_entry.get())

        if monto_cuenta <= 0 or porcentaje_propina < 0:
            resultado_label.config(
                text="Error: Por favor ingrese valores válidos.")
        else:
            propina = monto_cuenta * (porcentaje_propina / 100)
            total_con_propina = monto_cuenta + propina
            resultado_label.config(text="Propina: ${:.2f}\nTotal con propina: ${:.2f}".format(
                propina, total_con_propina))
    except ValueError:
        resultado_label.config(
            text="Error: Por favor ingrese valores numéricos válidos.")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Propinas")

# Crear widgets
monto_label = tk.Label(ventana, text="Monto de la cuenta:")
monto_label.pack()

monto_entry = tk.Entry(ventana)
monto_entry.pack()

porcentaje_label = tk.Label(ventana, text="Porcentaje de propina:")
porcentaje_label.pack()

porcentaje_entry = tk.Entry(ventana)
porcentaje_entry.pack()

calcular_button = tk.Button(
    ventana, text="Calcular Propina", command=calcular_propina)
calcular_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Ejecutar la aplicación
ventana.mainloop()
