estado = True
productos = []
precios = []
while estado:
    try:
        print("1.Ingresar Productos")
        print("2 Ver Compras")
        print("3 Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            producto = input("Ingrese un producto")
            precio = int(input("Ingrese el precio del producto: "))

            while precio <= 0:
                precio = int(input("El precio no es correcto...inténtelo de nuevo: "))

            productos.append(producto)
            precios.append(precio)
        elif opcion == 2:
            if len(productos) > 0:
                print(f"La lista de productos ingresados es: {productos}")
                print(f"Se ingresaron {len(productos)} productos")
                print(f"La suma total de los precios ingresados es {sum(precios)}")
            else:
                print("No hay suficientes datos para procesar")
        elif opcion == 3:
            print("Gracias por usar nuestra App")
            estado = False
        else:
            print("La opción ingresada no existe")
    except ValueError:
        print("Error: dato incorrecto")
    finally:
        print("Programa de Compras")