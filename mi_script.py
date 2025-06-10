import tkinter as tk

def actualizar_etiqueta():
    etiqueta.config(text="¡Hola, mundo!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de GUI")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón para saludar")
etiqueta.pack(pady=10)

# Crear un botón
boton_saludar = tk.Button(ventana, text="Saludar", command=actualizar_etiqueta)
boton_saludar.pack()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()