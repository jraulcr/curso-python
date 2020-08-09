class Coche():

	#constructor
	def __init__(self):
	
		#Propiedades La encapsulacion se añade a la variable __
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	#Comportamientos o métodos
	def arrancar(self, arrancamos):
		self.enmarcha=arrancamos

		if self.enmarcha:
			return "El coche está en marcha"
		else:
			return "El coche está parado"


	#	self.enmarcha=True

	def estado(self):
		print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ",
		 self.__anchoChasis, " y un largo de ", self.__largoChasis)
			
			# if self.enmarcha:
			# 	return "El coche está en marcha"
			# else:
			# 	return "El coche está parado"


#Instanciar una clase o ejemplarizar (Python prescinde de la palabra reservada en otros lenguajes "new")
miCoche=Coche()

# print("El largo del coche es: ",  miCoche.largoChasis)
# print("El coche tiene: " , miCoche.ruedas , " ruedas")
print(miCoche.arrancar(True))

miCoche.estado()


print("------------------ A continuación creamos el segundo objeto ---------------------")


miCoche2=Coche()

# print("El largo del coche es: ",  miCoche2.largoChasis)
# print("El coche tiene: " , miCoche2.ruedas , " ruedas")
print(miCoche2.arrancar(False))

miCoche2.ruedas=2;
miCoche2.estado()

