import tkinter as tk
from tkinter import ttk, messagebox
import requests

# API endpoint para obtener tasas de cambio
API_URL = "https://api.exchangerate-api.com/v4/latest/"


def obtener_tasas(moneda_base):
    try:
        response = requests.get(f"{API_URL}{moneda_base}")
        response.raise_for_status()
        datos = response.json()
        return datos["rates"]
    except requests.RequestException as e:
        messagebox.showerror(
            "Error", f"No se pudieron obtener las tasas de cambio: {e}")
        return None


def convertir():
    moneda_base = base_combobox.get()
    moneda_objetivo = objetivo_combobox.get()
    cantidad = cantidad_entry.get()

    if not cantidad:
        messagebox.showerror("Error", "Ingrese una cantidad a convertir.")
        return

    try:
        cantidad = float(cantidad)
    except ValueError:
        messagebox.showerror("Error", "Ingrese una cantidad válida.")
        return

    tasas = obtener_tasas(moneda_base)
    if tasas and moneda_objetivo in tasas:
        tasa_conversion = tasas[moneda_objetivo]
        resultado = cantidad * tasa_conversion
        resultado_label.config(
            text=f"{cantidad:.2f} {moneda_base} = {resultado:.2f} {moneda_objetivo}")
    else:
        messagebox.showerror("Error", "No se pudo realizar la conversión.")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Monedas")

# Crear widgets
cantidad_label = tk.Label(ventana, text="Cantidad:")
cantidad_label.grid(row=0, column=0, padx=10, pady=10)
cantidad_entry = tk.Entry(ventana)
cantidad_entry.grid(row=0, column=1, padx=10, pady=10)

base_label = tk.Label(ventana, text="Moneda Base:")
base_label.grid(row=1, column=0, padx=10, pady=10)
base_combobox = ttk.Combobox(
    ventana, values=["USD", "EUR", "GBP", "JPY", "AUD"], state="readonly")
base_combobox.grid(row=1, column=1, padx=10, pady=10)
base_combobox.set("USD")

objetivo_label = tk.Label(ventana, text="Moneda Objetivo:")
objetivo_label.grid(row=2, column=0, padx=10, pady=10)
objetivo_combobox = ttk.Combobox(
    ventana, values=["USD", "EUR", "GBP", "JPY", "AUD"], state="readonly")
objetivo_combobox.grid(row=2, column=1, padx=10, pady=10)
objetivo_combobox.set("EUR")

convertir_button = tk.Button(ventana, text="Convertir", command=convertir)
convertir_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

resultado_label = tk.Label(ventana, text="")
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
