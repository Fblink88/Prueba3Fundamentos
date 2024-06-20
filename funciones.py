
detalles=["pequeño", "mediano", "grande"]
pedidos=[]
sectores=["CENTRO", "NORTE", "SUR"]
def registrarPedido(pedidos):
    cantPequenos=0
    cantMedianos=0
    cantGrandes=0
    nombreCompleto=input("Ingrese nombre y apellido: ").upper()
    direccion=input("Ingrese dirección:     ").upper()
    sector=input("Ingrese el sector de la dirección (Centro/Norte/Sur): ").upper()
    while sector not in sectores:
        print("Secotr no válido")
        sector=input("Ingrese el sector de la dirección (Centro/Norte/Sur): ").upper()
    while True:
        print("Seleccione tamaño de el/los paquete(s)")
        print("1. Pequeño")
        print("2. Mediano")
        print("3. Grande")
        try:
            
            opcDetalle=int(input("Ingrese la opción: "))
            if opcDetalle==1:
                detalle=detalles[0]
                try: 
                    cantPequenos=int(input("Ingrese la cantidad de paquetes pequeños: "))
                except ValueError:
                    print("Error: Ingrese una opción válida")
            elif opcDetalle==2:
                detalle=detalles[1]
                try:
                    cantMedianos=int(input("Ingrese la cantidad de paquetes medianos: "))
                except ValueError:
                    print("Error: Ingrese una opción válida")
            elif opcDetalle==3:
                detalle=detalles[2]   
                try:    
                    cantGrandes=int(input("Ingrese la cantidad de paquetes Grandes: "))
                except ValueError:
                    print("Error: Ingrese una opción válida")
            else:
                print("Ingrese una opción correcta")
            opc2=input("¿Desea agregar otro paquete? (Escriba si, en caso contrario aprete Enter)").upper()
            if opc2=="SI":
                print()
            else:
                break
        except ValueError:
            print("Error: Ingrese una opción válida")
    pedidos.append({
        "Nombre": nombreCompleto,
        "Direccion": direccion,
        "Sector": sector,
        "Paquete Pequeno": str(cantPequenos),
        "Paquete Mediano": str(cantMedianos),
        "Paquete Grande": str(cantGrandes), 
    })
    print("Datos ingresados con éxito")
    
def listarPedidos(pedidos):
    for pedido in pedidos:
        print(pedido)

def imprimirRuta(pedidos):
    while True:
        print("Selecciones el sector del pedido que desea imprimir")
        print("1. Centro")
        print("2. Norte")
        print("3. Sur")
        print("4. Todos los sectores")
        print("5. Salir")
        pedidosImprimir=[]
        try:
            opc3=int(input("Ingrese opción: "))
            if opc3==1:
                pedidoBuscar=sectores[0]
                for pedido in pedidos:
                    for elemento in pedido.values():
                        if elemento == pedidoBuscar:
                            pedidosImprimir.append(pedido)
                            nombreArchivo = f"plantilla_{sectores[0]}.txt"
            elif opc3==2:
                pedidoBuscar=sectores[1]
                for pedido in pedidos:
                    for elemento in pedido.values():
                        if elemento == pedidoBuscar:
                            pedidosImprimir.append(pedido)
                            nombreArchivo = f"plantilla_{sectores[1]}.txt"
            elif opc3==3:
                pedidoBuscar=sectores[2]
                for pedido in pedidos:
                    for elemento in pedido.values():
                        if elemento == pedidoBuscar:
                            pedidosImprimir.append(pedido)                           
                            nombreArchivo = f"plantilla_{sectores[2]}.txt"
            elif opc3==4:
                pedidosImprimir=pedidos
                nombreArchivo="plantilla_todos_sectores.txt"
            elif opc3==4:
                break
            else:
                print("Ingrese una opción válida")

        except ValueError:
            print("Error: Ingrese una opción válida")
        try:
            with open(nombreArchivo,"w") as archivo:
                for pedido in pedidosImprimir:
                    archivo.write(f"Nombre: {pedido["Nombre"]} \n")
                    archivo.write(f"Direccion: {pedido["Direccion"]} \n")
                    archivo.write(f"Sector: {pedido["Sector"]} \n")
                    archivo.write(f"Paquetes pequenos: {pedido["Paquete Pequeno"]} \n")
                    archivo.write(f"Paquetes medianos: {pedido["Paquete Mediano"]} \n")
                    archivo.write(f"Paquetes grandes: {pedido["Paquete Grande"]} \n")
                    archivo.write("\n")
        
            print("Datos impresos con éxito")
            break
        except UnboundLocalError:
            print("No hay datos ingresados en sector seleccionado")