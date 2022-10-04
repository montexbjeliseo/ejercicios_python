print("Evaluar nota")
nota = float(input("Introduce tu nota: "))

def evaluar(nota):
	if nota < 6:
		return "Insuficiente!"
	elif nota < 7:
		return "Suficiente!"
	elif nota < 8:
		return "Bien!"
	elif nota < 10:
		return "Notable!"
	else:
		return "Sobresaliente!"

print("Tu nota es", evaluar(nota))
print("Fin del programa...")
