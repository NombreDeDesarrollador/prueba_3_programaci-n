import os, time, csv
from funciones import *
while True:
    os.system("cls")
    print("\tMENÚ")
    print("""1. Registrar pedido.
2. Listar todos los pedidos.
3. Buscar pedido por RUT.
4. Imprimir hoja de ruta.
5. Salir del programa.""")
    try:
        opc = int(input("Ingrese  una opción: "))
        if  opc==(1, 2, 3, 4, 5):
            break
        else:
            print("Las opciones solo son 1, 2, 3, 4, 5") 
    except:
        print("Solo se deben ingresar número enteros")
    os.system("cls")


    if opc==1:
        registrar_pedidos()
    elif opc==2:
        listar_pedidos()
    elif opc==3:
        pass
    elif opc==4:
        pass
    else:
        salir()

    time.sleep(3)
        