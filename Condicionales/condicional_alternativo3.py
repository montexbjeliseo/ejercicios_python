print("Verificar edad")

edad = int(input("Introduce tu edad: "))

def verificar(edad):
	if 0 < edad < 100:
		return "Edad correcta"
	else :
		return "Edad Incorrecta"

print(verificar(edad))
print("Fin del programa...")
