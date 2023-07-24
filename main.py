from paquetes.preentrega2_clase_cliente import Cliente


Julian = Cliente("Julian", "Gonzalez", "34", "00343532", "julian@gmail.com", "00001", "11232526")
Ramon = Cliente("Ramon", "Alvarez", "26", "00535269", "ramon@gmail.com", "00002", "1123652")
Carlos =Cliente("Carlos", "Garcia", "42", "00245954", "charly@gmail.com", "00003", "1123965")


Julian.compra("audicular", "Boedo")
print(Julian)
print(Julian.get_dni())
print(Julian.get_email())
print("--------------------------")


Ramon.compra("cargador", "Almagro")
print(Ramon)
print(Carlos.get_dni())
print(Carlos.get_email())
print("--------------------------")


Carlos.compra("piano", "San Telmo")
print(Carlos)
print(Carlos.get_dni())
print(Carlos.get_email())
print("--------------------------")