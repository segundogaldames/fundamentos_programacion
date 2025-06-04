estado = True
notas = []
while estado:
    try:
        print("1. Ingresar notas")
        print("2. Ver Resultados")
        print("3. Salir")

        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            nota = float(input("Ingrese la nota: "))
            while nota < 1 or nota > 7:
                nota = float("Nota errónea... intente nuevamente")

            notas.append(nota)
        elif opcion == 2:
            if len(notas) > 0:
                print(f"Las notas ingresadas son: {notas}")
                print(f"Se ingresaron {len(notas)} notas al sistema")
                promedio = sum(notas) /len(notas)
                print(f"El promedio de las notas ingresadas es {promedio} ")
            else:
                print("No hay datos suficientes para mostrar resultados")
        elif opcion == 3:
            print("Gracias por usar nuestra APP")
            estado = False
        else:
            print("Opción no válida")
    except ValueError:
        print("Error: dato incorrecto... intente de nuevo")
    finally:
        print("Programa de Cálculo de Notas")