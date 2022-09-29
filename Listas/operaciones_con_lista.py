miLista = ["María", "Pepe", "Marta", "Antonio"]
print("Lista completa (Original): ", miLista)
miLista.append("Sandra")
print("Lista completa (agregando a Sandra al final): ", miLista)
miLista.insert(2, "Juan")
print("Lista completa (Insertando a Juan en el índice 2): ", miLista)
miLista.extend(["Ana", "Lucía", "Pedro"])
print("Lista completa (Extendiendo): ", miLista)

print("Indice de Maria en la lista: ", miLista.index("María"))

print("Está Pepe en la lista: ", "Pepe" in miLista)

print("Está Nadie en la lista: ", "Nadie" in miLista)
print("Está Ana en la lista: ", "Ana" in miLista)
print("Elimina Ana!")
print("Está Ana en la lista: ", "Ana" in miLista)