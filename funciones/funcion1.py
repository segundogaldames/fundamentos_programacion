def suma(a,b):
    return a + b

def errorException():
    return "Error: dato incorrecto"

estado = True
while estado:
    try:
        valor1 = int(input("Ingrese el primer valor"))
        valor2 = int(input("Ingrese el segundo valor"))
        resultado = suma(valor1, valor2)
        print(f"La suma es {resultado}")

        print(f"La suma sin variable de retorno es {suma(valor1, valor2)}")
        estado = False
    except ValueError:
        print(errorException())
    finally:
        print("App de sumas")