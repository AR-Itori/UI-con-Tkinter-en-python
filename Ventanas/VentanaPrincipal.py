# ESTE ARCHIVO CONTIENE LA VENTANA PRINCIPAL PARA INICIAR UNA APLICACION EN WINDOWS

import tkinter as tk

# Funcion que devuelve cordenadas para centrar una ventana
def centrarV(mult):
    # Definir un tamaño de ventana basado en la resolución x el % deseado
    ancho = int(Anp * mult)  # % del ancho de la pantalla
    alto = int(Alp * mult)    # % del alto de la pantalla

    # Calcular las coordenadas para centrar la ventana
    cx = (Anp - ancho) // 2
    cy = (Alp - alto) // 2

    cordenadas = f"{ancho}x{alto}+{cx}+{cy}"
    return cordenadas

# Funcion que requiere de una ventana para destruirla
def destruirAPP(ventana):
    print("Finalizando aplicacion...")
    ventana.destroy()
    return


# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#

# Crear la ventana principal
ventanaPrin = tk.Tk()
ventanaPrin.title("Ventana Principal") # Nombre de la ventana

# Obtener el tamaño de la pantalla
Anp = ventanaPrin.winfo_screenwidth()
Alp = ventanaPrin.winfo_screenheight()

# Configurar la geometría de la ventana para que esté centrada
ventanaPrin.geometry(centrarV(0.5))

# Elimina la barra superior de la ventana
ventanaPrin.overrideredirect(False)

# Configura el zoom de la pantalla
ventanaPrin.state("normal")


# Boton para destruir la ventana correctamente
boton = tk.Button(ventanaPrin, text="> CERRAR <", command=lambda: destruirAPP(ventanaPrin))
boton.pack(side="bottom", anchor="center", pady=30) # Aplica el boton a la ventana, lo manda
# al fondo de la ventana, lo centra y le da un margen en la cordenada " y " (verticalmente)

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#


# Ejecuta la ventana en bucle (necesario para funcionar)
# Esta debe ser la ultima linea de codigo, todo el funcionamiento va antes de esto
# Puedes importar la ventana principal a otro archivo y desde ahi ejecutar el bucle
# (siempre al final de todo el codigo)
ventanaPrin.mainloop()