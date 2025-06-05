estado = True
alumnos = []
notas = []
while estado:
    try:
        for x in range(3):
            nom = input(f"Ingrese el nombre del alumno {x+1}: ")
            
            nota1 = float(input("Ingrese la nota 1: "))
            nota2 = float(input("Ingrese la nota 2: "))

            while (nota1 < 1 or nota1 > 7) or (nota2 < 1 or nota2 > 7):
                print("Las notas ingresadas no son válidas")
                nota1 = float(input("Ingrese la nota 1: "))
                nota2 = float(input("Ingrese la nota 2: "))

            alumnos.append(nom)
            notas.append([nota1, nota2])

        for x in range(3):
            print(f"Alumno {x+1}: {alumnos[x]}. Sus notas son {notas[x][0]}, {notas[x][1]}")

        estado = False
    except ValueError:
        print("Error: dato incorrecto")
    finally:
        print("App de notas")