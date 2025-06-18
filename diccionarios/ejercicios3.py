def cargar():
    personas = {}
    print("Registre 3 personas")
    for x in range(3):
        numero = input(f"Ingrese el número de documento de la persona {x+1}: ")
        nombre = input(f"Registre el nombre de la persona con numero {numero}: ")
        personas[numero] = nombre

    return personas

def mostrar(personas):
    print("Lista de personas")
    for persona in personas:
        print(persona, personas[persona])

def busqueda(personas):
    numero = input("Ingrese el número de la persona que busca: ")
    if numero not in personas:
        #print(f"El nombre de la persona es {personas[numero]}")
        return "No hay una persona registrada con este número"
    
    return "El nombre de la persona es: " + personas[numero]

estado = True
while estado:
    try:
        personas = cargar()
        mostrar(personas)
        print(busqueda(personas))
    except ValueError:
        print("")