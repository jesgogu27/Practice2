milista = ["Maria", "pepe", "Martha", "Antonio"]

print(milista)

#imprimir un elemento= se manda a imprimir el indice 
print(milista[2])

#imprimir una porcion, imprime incluyendo el indice inicial indicado hasta el valor penultimo del indice final.
print(milista[1:3])

#mostras los elementos de la lista antes del indice indicado por el usuario
print(milista[:2])

#mostras los elementos de la lista despues del indice indicado por el usuario
print(milista[1:])

#mostras los elementos de la lista despues del indice indicado por el usuario
print(milista[1+1:])


#agregar datos a la lista. Append donde la queremos agregar
milista.append("Jesus")
print(milista)

#agregar datos a la lista a una parte especifica de la lista
milista.insert(2,"Dilia")
print(milista)

#extend para agregar variaos elementos a la lista
milista.extend(["sandra", "ana", "Lucia"])
print(milista)

#devolver el indice en el cual se encuentra un elemento de la lista
elemen = milista.index("Martha")
print(elemen)

#comprobar si un elemento se encuentra o no en una lista
print("pepe" in milista)
print("pepee" in milista)

#extend para agregar variaos elementos a la lista
milista.extend([555, 2.58600, True])
print(milista)

#remove se usa para eliminar
milista.remove(True)
print(milista)

#pop elimina el ultimmo elemento de la lista
milista.pop()
print(milista)

#combinar dos listas 
milista2 = ["mayo", "junio", "julio"]
milista3 = milista + milista2
print(milista3)

#repetir la lista 
milista2 = ["mayo", "junio", "julio"]*3
print(milista2)

