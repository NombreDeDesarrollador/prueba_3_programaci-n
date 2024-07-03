import time, os
pedidos = []

def registrar_pedidos():
    print("\tREGISTRAR  PEDIDO")
    rut  = int(input("Ingrese rut: "))

    while True:
        try:
            nombre =  input("Ingrese nombre: ")
            if len(nombre)>=3 and nombre.isalpha:
                break
            else:
                print("El nombre debe tener mas de 3 letras")
        except:
            print("Solo debe ingresar letras")
    while True:
        try:
            dirección = input("Ingrese  dirección: ")
            if len(dirección)>=3 and dirección.isalpha:
                break
            else:
                print("La dirección debe tener mas de 3 letras")
        except:
                print("Solo debe ingresar letras")
    while True:
        try:
            comuna = input("Ingrese comuna: ")
            if len(comuna)>=3 and comuna.isalpha:
                break
            else:
                print("La comuna debe tener mas de 3 letras")
        except:
            print("Solo debe ingresar letras")
    
    

    while True:
        try:
            opc_2 = int(input("¿Desea llevar cilindros de 5 kg? si(1)/no(2): "))
            if opc_2==(1):
                cantidad_5_kg = int(input("¿Cuantos cilindros de 5 kg desea llevar?"))
                if cantidad_5_kg==0:
                    break
            elif opc_2==2:
                break    
        except:
            print("Las opciones son solo 1 y 2. Solo se deben ingresar números enteros!")

    while True:
        try:
            opc_3 = int(input("¿Desea llevar cilindros de 15 kg? si(1)/no(2): "))
            if opc_3==(1):
                cantidad_15_kg= int(input("¿Cuantos cilindros de 15 kg desea llevar?"))
                if cantidad_15_kg==0:
                    break
            elif opc_2==2:
                break    
        except:
            print("Las opciones son solo 1 y 2. Solo se deben ingresar números enteros!")

    
    pedidos_realizados = ["rut", rut, 
                          "nombre", nombre, 
                          "direccion", dirección, 
                          "comuna", comuna, 
                          "cilindros 5Kg", cantidad_5_kg, 
                          "cilindros 15Kg", cantidad_15_kg, 
                          "total", (cantidad_5_kg*12500)+(cantidad_15_kg*25500)]
    
    pedidos.append(pedidos_realizados)

    print("PEDIDO REALIZADO CON ÉXITO! ")
def listar_pedidos ():
    if not pedidos:
        print("NO HAY PEDIDOS REGISTRADOS!")
    else:
        print(pedidos)


def  buscar_pedido():
    pass

def imprimir_hoja_de_ruta():
    pass

def salir():
    print("Saliste del programa")
    exit()