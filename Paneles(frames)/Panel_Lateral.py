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

# Funcion para mostrar/ocultar panel
# Se pasan los wigets principales para desabilitarlos y evitar su uso mientras el panel lateral esta abierto
def usar_lateral(panel, accion, wigets):
    if accion == "mostrar":
        panel.place(relx=0, rely=0, relwidth=0.2, relheight=1)
        for wgt in wigets:
            wgt.configure(state="disabled")
    elif accion == "ocultar":
        panel.place_forget()
        for wgt in wigets:
            wgt.configure(state="normal")
    else: print("No se paso el panel")

    return

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Principal") # Nombre de la ventana

# Obtener el tamaño de la pantalla
Anp = ventana.winfo_screenwidth()
Alp = ventana.winfo_screenheight()

# Configurar la geometría de la ventana para que esté centrada
ventana.geometry(centrarV(0.5))

# Elimina la barra superior de la ventana
ventana.overrideredirect(False)

# Configura el zoom de la pantalla
ventana.state("normal")

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#

# Crear el panel Principal
principal = tk.Frame(ventana, bg="lightcoral")
principal.place(relx=0, rely=0, relwidth=1, relheight=1)
# Los prinmeros dos valores del .place() controlan a que distancia aparecen en X y Y cordenadas
# El segundo par de valores controlan el tamño en X y Y cordenadas

# Boton para mostrar el panel lateral
btn_abrir_lateral = tk.Button(principal, text="> > >", command=lambda: usar_lateral(panel_lateral, "mostrar", wigets_principales))
btn_abrir_lateral.pack(side="top", anchor="nw")

# Boton para destruir la ventana correctamente
boton_cerrar = tk.Button(principal, text="> CERRAR <", command=lambda: destruirAPP(ventana))
boton_cerrar.pack(side="bottom", anchor="center", pady=30) # Aplica el boton a la ventana, lo manda
# al fondo de la ventana, lo centra y le da un margen en la cordenada " y " (verticalmente)


# Crea una lista con todos los wigets para habilitarlos/deshabilitarlos
wigets_principales = [btn_abrir_lateral, boton_cerrar]

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#


# Crear el panel lateral
panel_lateral = tk.Frame(principal, bg="lightblue")
panel_lateral.place(relx=0, rely=0, relwidth=0.5, relheight=1)
# Los prinmeros dos valores del .place() controlan a que distancia aparecen en X y Y cordenadas
# El segundo par de valores controlan el tamño en X y Y cordenadas

# Boton para ocultar el panel lateral
btn_cerrar_lateral = tk.Button(panel_lateral, text="< < <", command=lambda: usar_lateral(panel_lateral, "ocultar", wigets_principales))
btn_cerrar_lateral.pack(side="top", anchor="nw")

panel_lateral.place_forget() # Oculta el panel por defecto


# Ejecuta la ventana en bucle (necesario para funcionar)
# Esta debe ser la ultima linea de codigo, todo el funcionamiento va antes de esto
# Puedes importar la ventana principal a otro archivo y desde ahi ejecutar el bucle
# (siempre al final de todo el codigo)
ventana.mainloop()