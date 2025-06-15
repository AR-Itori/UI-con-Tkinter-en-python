import random

nombres = ["Pepe", "Jose", "Joaquin", "Adrian", "Isaac", "Roberto", "Hernan", "Lucas", "Franco"]

subfijo_alias = ["El", "La", "The", "Rey", "Sombra"]
alias = ["Espinaca", "Gancho", "Papa", "Sindi"]

dominios = ["@gmail.com", "@outlook.com", "@yahoo.com"]

ocupaciones = ["Programador", "Artista", "Hacker", "Diseñador", "Músico"]

caracteres = ["h", "w", "m", "r", "i", "l", "o", "s", "n", "c", "p", "x", "b", "k", "t", "j"]
simbolos = ["@", "!¡", "&", "¿?", "#", "%"]

def crear_nombre():
    nombre1 = random.choice(nombres)
    nombre2 = random.choice(nombres)

    while nombre2 == nombre1:
            nombre2 = random.choice(nombres)

    nombre_completo = nombre1 + " " + nombre2
    return nombre_completo

def crear_alias():
      val1 = random.choice(subfijo_alias)
      val2 = random.choice(alias)

      al = val1 + " " + val2
      return al

def crear_email(subfijo):
      val = random.choice(dominios)
      val1 = str(random.randint(0, 99))
      email = subfijo + val1 + val

      return str(email).lower()

def crear_contraseña():
    contra = random.choice(simbolos)
    for x in range(0, random.randint(13, 24)):
            contra = contra + random.choice(caracteres)

    return contra
            
            


nombre = crear_nombre()
al = crear_alias()
email = crear_email(nombre.replace(" ", "") + "_"+al.replace(" ", ""))
ocupacion = random.choice(ocupaciones)
contra = crear_contraseña()

with open("identidad_secreta.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"""
        IDENTIDAD SECRETA
        Nombre: {nombre}
        Alias: {al}
        Email: {email}
        Ocupacion: {ocupacion}
        Contraseña: {contra}
        ------------------------
        """)


print ("Creando datos...")
print(f"El nombre creado fue: {nombre}")
print(f"El alias creado fue {al}")
print(f"El correo creado fue {email}")
print(f"La ocupacion creada fue {ocupacion}")
print(f"La contrasena creada fue {contra}")