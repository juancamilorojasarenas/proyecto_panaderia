import json

def cargar_pedidos():
    try:
        with open("pedidos.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

pedidos = cargar_pedidos()

def guardar_pedidos():
    with open("pedidos.json", "w") as file:
        json.dump(pedidos, file, indent=4)

def agregar_pedido():
    code_pedido = input("Ingrese el código del pedido: ")
    code_cliente = input("Ingrese el código del cliente: ")
    fecha = input("Ingrese la fecha del pedido: ")

    pedido = {
        "codigo_pedido": code_pedido,
        "codigo_cliente": code_cliente,
        "fecha_pedido": fecha,
        "detalles_pedido": []
    }

    pedidos.append(pedido)
    guardar_pedidos()
    print("El pedido fue agregado exitosamente.")

def detalles_pedido(): 
    code_pedido = input("Ingrese el código del pedido: ")
    pedido_encontrado = next((p for p in pedidos if p["codigo_pedido"] == code_pedido), None)

    if pedido_encontrado:
        code_producto = input("Ingrese el código del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = int(input("Precio: "))
        num_linea = int(input("Ingrese el número de línea del pedido: "))

        detalle = {
            "codigo_producto": code_producto,
            "cantidad": cantidad,
            "precio_unidad": precio,
            "numero_linea": num_linea
        }
        
        pedido_encontrado["detalles_pedido"].append(detalle)
        guardar_pedidos()
        print("El detalle del pedido fue agregado exitosamente.")
    else: 
        print("El pedido no existe.")

def pedir():
    while True:
        continuar = input("¿Desea realizar un pedido (si/no)?: ").lower()
        if continuar == "si":
            agregar_pedido()
            while True:
                agreg = input("¿Desea agregar detalles del pedido (si/no)?: ").lower()
                if agreg == "si":
                    detalles_pedido()
                elif agreg == "no":
                    print("Volviendo al menú de gestión de pedidos...")
                    break
                else:
                    print("Por favor, vuelva a intentarlo.")
        elif continuar == "no":
            print("Volviendo a la gestión de pedidos...")
            break
        else:
            print("Opción no disponible, intente de nuevo.")

def mostrar_pedidos():
    if not pedidos:
        print("No hay pedidos registrados.")
    else:
        for p in pedidos:
            print(f"Código: {p['codigo_pedido']}, Cliente: {p['codigo_cliente']}, Fecha: {p['fecha_pedido']}")

def modificar_pedidos():
    while True:
        modi = input("¿Desea modificar un pedido (si/no)?: ").lower()
        if modi == "si":
            code_pedido = input("Ingrese el código del pedido a modificar: ")
            pedido_encontrado = next((p for p in pedidos if p["codigo_pedido"] == code_pedido), None)

            if pedido_encontrado:
                print(modi_pedidos)
                opc = input("Ingrese la opción que desea modificar: ")

                if opc == "1":
                    print(sub_menu_modi)
                    op = input("Escoja una opción: ")
                    
                    if op == "1":
                        num_linea = int(input("Ingrese el número de línea a modificar: "))
                        detalle = next((d for d in pedido_encontrado["detalles_pedido"] if d["numero_linea"] == num_linea), None)

                        if detalle:
                            nuevo_num_linea = int(input("Ingrese el nuevo número de línea: "))
                            detalle["numero_linea"] = nuevo_num_linea
                            print("Número de línea actualizado.")
                        else:
                            print("Número de línea no encontrado.")

                    elif op == "2":
                        code_producto = input("Ingrese el nuevo código del producto: ")
                        for detalle in pedido_encontrado["detalles_pedido"]:
                            detalle["codigo_producto"] = code_producto
                        print("Código del producto actualizado.")

                    elif op == "3":
                        cantidad = int(input("Ingrese la nueva cantidad: "))
                        for detalle in pedido_encontrado["detalles_pedido"]:
                            detalle["cantidad"] = cantidad
                        print("Cantidad actualizada.")

                    elif op == "4":
                        print("Terminando modificaciones...")

                elif opc == "2":
                    code_cliente = input("Ingrese el nuevo código del cliente: ")
                    pedido_encontrado["codigo_cliente"] = code_cliente
                    print("Código del cliente actualizado.")

                elif opc == "3":
                    fecha = input("Ingrese la nueva fecha: ")
                    pedido_encontrado["fecha_pedido"] = fecha
                    print("Fecha actualizada.")

                elif opc == "4":
                    print("Volviendo a la modificación de pedidos.")
                    break

                guardar_pedidos()

            else:
                print("Pedido no encontrado.")
        
        elif modi == "no":
            print("Volviendo a la gestión de pedidos...")
            break

        else:
            print("Opción inválida, vuelva a intentarlo.")

def eliminar_pedidos():
    code_pedido = input("Ingrese el código del pedido a eliminar: ")
    pedido_encontrado = next((p for p in pedidos if p["codigo_pedido"] == code_pedido), None)

    if pedido_encontrado:   
        pedidos.remove(pedido_encontrado)
        guardar_pedidos()
        print("El pedido fue eliminado exitosamente.")  
    else:
        print("El pedido no existe o ya fue eliminado anteriormente.")

modi_pedidos = """
**********************************************
1. Editar detalles del pedido
2. Editar código del cliente
3. Editar fecha del pedido
4. Volver al menú de gestión de pedidos
**********************************************
"""

sub_menu_modi = """
**********************************
1. Cambiar el número de línea
2. Cambiar código del producto
3. Cambiar cantidad
4. Terminar modificaciones
*********************************
"""
