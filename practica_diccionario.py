midiccionario={"Alemania":"Berlin","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
midiccionario["Italia"]="Lisboa"

print(midiccionario)
#Insertamos nuevo elemento
midiccionario["Italia"]="Roma"
print(midiccionario)
#Modificamos. Para corregir el valor erroneo sobreescribimos editandolo de nuevo
print(midiccionario["España"])
#Eliminamos
del midiccionario["Reino Unido"]
print(midiccionario)

#Diccionario co tupla
mitupla=("España", "Francia", "Reino Unido", "Alemania")
midiccionario2={mitupla[0]:"Madrid",mitupla[1]:"París",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(midiccionario2)
print(midiccionario["Alemania"])
print(mitupla[0])

midiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago Bulls","Anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario3)
print(midiccionario3["Equipo"])
print(midiccionario3["Anillos"])

#Doble tupla
midiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago Bulls","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario4)
print(midiccionario4["Anillos"])
print(midiccionario4.keys())
print(midiccionario4.values())
print(len(midiccionario4))