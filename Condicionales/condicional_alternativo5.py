print("Verificar beca")

distancia = float(input("Distancia de la escuela: "))
hermanos = int(input("Cuantos hermanos tiene: "))
salario_familiar = float(input("Salario familiar: "))

if distancia > 40 and hermanos > 2 or salario_familiar <= 20000:
	print("Le corresponde una beca")
else :
	print("No le corresponde una beca")