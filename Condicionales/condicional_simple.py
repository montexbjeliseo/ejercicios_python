print("Evaluar nota de alumno")

nota_alumno = float(input("Ingrese la nota del alumno: "))

def evaluar(nota):
	valoracion = "aprobado"
	if nota < 6:
		valoracion = "desaprobado"
	return valoracion

print("El alumno ha", evaluar(nota_alumno))