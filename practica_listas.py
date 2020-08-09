miLista=["María", "Pepe", "Marta", "Antonio"]

#Accede a todos los elementos
print(miLista[:])
#Acceso por indice (Desde el primer lugar)
print(miLista[2])
#Acceso por subindice (Desde el último lugar)
print(miLista[-1])
#Acesso por porciones
print(miLista[1:3])
print(miLista[2:])
print(miLista[:2])

#Agrega nuevo elemento al final de la lista
miLista.append("Sandra")
print(miLista[:])
#Agrega nuevo elemento desde N posicion de la lista
miLista.insert(2,"Curro")
print(miLista[:])
#Concatena una lista a la lista principal
miLista.extend(["Ana","Juan","Rebeca"])
print(miLista[:])
#Devuelve en que numero de indice está situado
print(miLista.index("Antonio"))
#Imprime True o False si un elemento está en la lista
print("Pepe" in miLista )
#Elimina un elemento a la lista
miLista.remove("Ana")
print(miLista[:])
#Elimina el último elemento de la lista
miLista.pop()
print(miLista[:])

#Concatena una lista con otra lista y lo devuelve unida a otra lista vacia
miLista1=["María", "Pepe", "Marta", "Antonio"]
miLista2=["Ana","Juan","Rebeca"]
miLista3=miLista1+miLista2
print(miLista3[:])
#Repite una lista N veces
miLista1=["Ana","Juan","Rebeca"]*3
print(miLista1[:])

numeros_lista = list((1,2,3,4))
print(numeros_lista)