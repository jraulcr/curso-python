# mitupla = ("Juan", 13,1,1995)
# print(mitupla[2])
# #Convierte una Tupla en Lista 'List'
# milista=list(mitupla)
# print(milista)

#Convierte una Lista en Tupla 'Tuple'
# milista = ["Juan", 13, 1, 1995, 13]
# mitupla=tuple(milista)
# print(mitupla)
# #Comprueba si un elemento esta incluido
# print("Juan" in mitupla)
# #Busca y comprueba cuantos elementos contiene undeterminado elemento a buscar
# print(mitupla.count(13))
# #Longitud de una tupla
# print(len(mitupla))

#Tuplas unitarias (Tupla con un único elemento)
# mitupla=("Juan",)
# print(len(mitupla))

#Empaquetado de Tupla (No es nada aconsejable)
#mitupla="Juan", 13, 1, 1995, 13
#print(mitupla)

#Desempaquetado de Tupla
mitupla = ("Juan", 13, 1, 1995)
nombre, dia, mes, anyo = mitupla
print(nombre)
print(dia)
print(mes)
print(anyo)

