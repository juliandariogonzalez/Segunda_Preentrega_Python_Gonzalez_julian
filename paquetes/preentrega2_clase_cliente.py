class Cliente:

  def __init__(self, nombre, apellido, edad, dni, email, numero_cliente, telefono):
    self.nombre = nombre
    self.__apellido = apellido
    self.edad = edad
    self.__dni = dni
    self.__email = email
    self.numero_cliente = numero_cliente
    self.__telefono = telefono

  def __str__(self):
    return(f"Mi nombre es: {self.nombre}, tengo {self.edad} años y mi numero de cliente es: {self.numero_cliente}")

  def get_apellido(self):
    print(f"Mi apellido es: {self.__apellido}")

  def get_dni(self):
    return(f"Mi numero de DNI es: {self.__dni}")

  def get_email(self):
    return(f"Mi email es {self.__email}")

  def telefono(self):
    print(f"Mi numero de telefono es: {self.__telefono}")

  def compra(self, articulo, sucursal):
    print(f"Hola, compre {articulo} en la sucursal {sucursal}")