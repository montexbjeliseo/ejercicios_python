print("Verificar salario")

salario_presidente = float(input("Salario del Presidente: "))
salario_director = float(input("Salario del Director: "))
salario_administrativo = float(input("Salario del Administrativo: "))
salario_jefe_area = float(input("Salario del Jefe de Area: "))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo correcto!")
else :
	print("Algo anda mal")