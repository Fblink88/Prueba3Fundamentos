

import funciones as fn
pedidos=[]
while True:
    print("\nMenu: Empresa de reparto PaquExpress")
    print("------------------------------------")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")
    try:
        print()
        opc=int(input("Ingrese su opción: "))
        if opc==1:
            fn.registrarPedido(pedidos)
        elif opc==2:
            fn.listarPedidos(pedidos)
        elif opc==3:
            fn.imprimirRuta(pedidos)
        elif opc==4:
            print("Hasta luego")
            break

    except ValueError:
        print("Error: Ingrese una opción válida")