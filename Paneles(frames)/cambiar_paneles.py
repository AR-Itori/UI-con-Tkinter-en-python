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
def destruirAPP(valor):
    print("Finalizando aplicacion...")
    valor.destroy()
    return

def cambiar_panel(paneles, num):
    print("cerrando todos los paneles")
    for x in paneles:
        x.place_forget()
    paneles[num].place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)


# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Principal") # Nombre de la ventana

# Obtener el tamaño de la pantalla
Anp = ventana.winfo_screenwidth()
Alp = ventana.winfo_screenheight()

# Configurar la geometría de la ventana para que esté centrada
ventana.geometry(centrarV(0.6))

# Elimina la barra superior de la ventana
ventana.overrideredirect(False)

# Configura el zoom de la pantalla
ventana.state("normal")

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#

panel_01 = tk.Frame(ventana, bg="red")
panel_01.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

panel_02 = tk.Frame(ventana, bg="green")
panel_02.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
panel_02.place_forget()

panel_03 = tk.Frame(ventana, bg="blue")
panel_03.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
panel_03.place_forget()

lista_paneles = (panel_01, panel_02, panel_03)

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#

panel_btns = tk.Frame(ventana, bg="coral")
panel_btns.place(relx=0.38, rely=0.75, relwidth=0.24, relheight=0.1)

btn1 = tk.Button(panel_btns, text="1", command=lambda: cambiar_panel(lista_paneles, 0))
btn1.pack(side="left", anchor="w", fill="both", expand=True)

btn2 = tk.Button(panel_btns, text="2", command=lambda: cambiar_panel(lista_paneles, 1))
btn2.pack(side="left", anchor="center", fill="both", expand=True)

btn3 = tk.Button(panel_btns, text="3", command=lambda: cambiar_panel(lista_paneles, 2))
btn3.pack(side="left", anchor="e", fill="both", expand=True)

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#

pnl_final = tk.Frame(ventana)
pnl_final.place(relx=0.88, rely=0, relwidth=0.12, relheight=0.1)

btn_cerrar = tk.Button(pnl_final, text=" >X< ", command=lambda: destruirAPP(ventana))
btn_cerrar.pack(anchor="center", fill="both", expand=True, padx=25, pady=20)

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /#

# Ejecuta la ventana en bucle
ventana.mainloop()