lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# imprimimos la lista completa
print("Lista completa")
print(lista)
print("El primer elemento de la lista")
# imprimimos la primer componente
print(lista[0])
print("El primer elemento de la sublista")
# imprimimos la primer componente de la lista contenida
# en la primer componente de la lista principal
print(lista[0][0])
print("Mostramos con un for los elementos de la sublista en la posicion 1")
# imprimimos con un for la lista contenida en la primer componente
for x in range(len(lista[0])):
    print(lista[0][x])
print("Mostramos todos los elementos de la lista con sus sublistas en un for anidado")               
# imprimimos cada elemento entero de cada lista contenida en la lista
for k in lista:
    for x in k:
        print(x)