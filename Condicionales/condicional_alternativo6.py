asignaturas = ["informática gráfica", "pruebas de software", "usabilidad y accessibilidad"]

print("Asignaturas optativas: ", asignaturas)

escogida = input("Escoja una asignatura: ")

if escogida.lower() in asignaturas:
	print("Asignatura elegida: ", escogida)

else :
	print("Asignatura no contemplada")