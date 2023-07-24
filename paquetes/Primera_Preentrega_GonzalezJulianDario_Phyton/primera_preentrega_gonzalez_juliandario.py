Base_de_datos = {}

#funcion para crear usuarios y contraseñas
def datos_usuarios():
  while True:
    usuario= input("Genere su nombre usuario: ")
    usuario = usuario.lower()
    if usuario in Base_de_datos:                  #con este condicional si el usuario existe en la BD, le solicito que ingrese uno nuevo
      print("Nombre de usuario existente. Genere un usuario diferente")
    else:
      contrasenia= input("Genere una contraseña: ")
      print("-----------------------------------")
      Base_de_datos.update({usuario:contrasenia})
      break
      print("-----------------------------------")

#funcion para mostrar los datos de los usuarios con sus contraseñas
def mostrar_datos():
    for dato in Base_de_datos.keys():
        print("El nombre de usuario es: "+ dato + "\n" +  "La contraseña es: " + Base_de_datos[dato])
        print("-----------------------------------")

#funcion de logueo
def login():
    usuario_ingreso = input("Ingrese su nombre de usuario: ")
    usuario_ingreso = usuario_ingreso.lower()
    if(Base_de_datos.get(usuario_ingreso) == None):
        while Base_de_datos.get(usuario_ingreso) == None:
            usuario_ingreso = input("Usuario incorrecto =(, ingrese su usuario de nuevo: ")
        print("Usuario correcto =)")
    contrasenia_ingreso = input("Ingrese su contraseña: ")
    while contrasenia_ingreso != Base_de_datos[usuario_ingreso]:
            contrasenia_ingreso = input("Contraseña erronea =(, ingrese la contraseña correcta: ")
    print("La contraseña es correcta =)")
    print("Iniciaste sesión de manera correcta =)")

#Imprimo los datos y contraseñas de los usuarios
print("Bienvenidos!!")
datos_usuarios()                             #llamo a la funcion para solicitar la generacion de usuarios y contraseñas x3
datos_usuarios()
datos_usuarios()
print("LOS USUARIOS GENERADOS Y  LAS CONTRASEÑAS SON: ")
mostrar_datos()                             #con esta funcion muestro los datos de usuario con sus contraseñas
print("LOGUIN DE USUARIOS: ")
print("--------------------")
login()                                     #esta funcion muestra la el loguin para los usuarios

with open("/content/diccionario.txt", "w") as diccionariotxt:
    for dato in Base_de_datos.keys():
      diccionariotxt.write(dato)
    for dato in Base_de_datos.values():
      diccionariotxt.write(dato)
diccionariotxt.close

