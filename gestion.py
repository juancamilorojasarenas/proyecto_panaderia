import json
from registro import productos, guardar_productos
#importar json y modulacion de registro

def cargar_pedidos():
    try:
        with open("pedidos.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
#funcion para cargar el json

pedidos = cargar_pedidos()

def guardar_pedidos():
    with open("pedidos.json", "w") as file:
        json.dump(pedidos, file, indent=4)
#funcion para guardar el json

def agregar_pedido(): #funcion para agregar el pedido
    code_pedido = input("Ingrese el código del pedido: ")
    code_cliente = input("Ingrese el código del cliente: ")
    fecha = input("Ingrese la fecha del pedido: ")

    pedido = {
        "codigo_pedido": code_pedido,
        "codigo_cliente": code_cliente,
        "fecha_pedido": fecha,
        "detalles_pedido": [],
        "total": 0.0
    }

    pedidos.append(pedido)
    guardar_pedidos()
    print("El pedido fue agregado exitosamente.")

def detalles_pedido():  #funcion para agregar detalles en el pedido realizando verificaciones necesarias
    code_pedido = input("Ingrese el código del pedido: ")
    pedido_encontrado = next((p for p in pedidos if p["codigo_pedido"] == code_pedido), None)

    if pedido_encontrado:
        code_producto = input("Ingrese el código del producto: ")
        producto_encontrado = next((p for p in productos if p["codigo_producto"] == code_producto), None)
        if not producto_encontrado:
            print("el producto no existe en el inventario")
            return
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad <= 0:
                print("la cantidad debe ser mayor a 0")
                return
            if cantidad > producto_encontrado["cantidad_en_stock"]:
                print(f"Stock insuficiente. Solo hay {producto_encontrado['cantidad_en_stock']} unidades disponibles.")
                return
            num_linea = int(input("Ingrese el número de línea del pedido: "))
        except ValueError:
            print("por favor ingrese valores numericos")
            return
            
        precio = producto_encontrado["precio_venta"]
        
        producto_encontrado["cantidad_en_stock"] -= cantidad
        guardar_productos()

        if producto_encontrado["cantidad_en_stock"] < 5:
            print(f"Quedan pocas unidades de '{producto_encontrado['nombre']}', solo hay {producto_encontrado['cantidad_en_stock']} unidades en stock.")
        
        detalle = {
            "codigo_producto": code_producto,
            "cantidad": cantidad,
            "precio_unidad": precio,
            "numero_linea": num_linea
        }
        
        pedido_encontrado["detalles_pedido"].append(detalle)
        pedido_encontrado["total"] = sum(d["precio_unidad"] * d["cantidad"] for d in pedido_encontrado["detalles_pedido"])
        guardar_pedidos()
        print("El detalle del pedido fue agregado exitosamente.")
    else: 
        print("El pedido no existe.")

def pedir(): #funcion para agregar pedidos y sus opciones
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

def mostrar_pedidos(): # funcion para mostrar la lista pedidos
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    print("\n************ LISTA DE PEDIDOS ************")
    print(f"{'Código':<12} | {'Cliente':<12} | {'Fecha':<12} | {'Total':<12}")
    print("-" * 50)

    for p in pedidos:
        total_formateado = f"${p['total']:,}"  # Formato con separador de miles
        print(f"{p['codigo_pedido']:<12} | {p['codigo_cliente']:<12} | {p['fecha_pedido']:<12} | {total_formateado:<12}")

    print("-" * 50)


def modificar_pedidos(): #funcion para modificar los pedidos
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
                        guardar_pedidos()

                    elif op == "2":
                        code_producto = input("Ingrese el nuevo código del producto: ")
                        for detalle in pedido_encontrado["detalles_pedido"]:
                            detalle["codigo_producto"] = code_producto
                        print("Código del producto actualizado.")
                        guardar_pedidos()

                    elif op == "3":
                        num_linea = int(input("Ingrese el número de línea a modificar: "))
                        detalle = next((d for d in pedido_encontrado["detalles_pedido"] if d["numero_linea"] == num_linea), None)

                        if not detalle:
                            print("Número de línea no encontrado.")
                            return

                        producto = next((p for p in productos if p["codigo_producto"] == detalle["codigo_producto"]), None)

                        if not producto:
                            print("Producto no encontrado en el inventario.")
                            return

                        producto["cantidad_en_stock"] += detalle["cantidad"]

                        try:
                            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                            if nueva_cantidad <= 0:
                                print("La cantidad debe ser mayor a 0.")
                                return

                            if nueva_cantidad > producto["cantidad_en_stock"]:
                                print(f"Stock insuficiente. Solo hay {producto['cantidad_en_stock']} unidades disponibles.")
                                return
                            
                            producto["cantidad_en_stock"] -= nueva_cantidad
                            detalle["cantidad"] = nueva_cantidad
                            pedido_encontrado["total"] = sum(d["precio_unidad"] * d["cantidad"] for d in pedido_encontrado["detalles_pedido"])
                            guardar_productos()
                            guardar_pedidos()
                            print("la cantidad ha sido  actualizada correctamente.")

                        except ValueError:
                            print("Ingrese solo números.")    
                            return
                                
                    elif op == "4":
                        print("Terminando modificaciones...")
                        break
                    
                elif opc == "2":
                    code_cliente = input("Ingrese el nuevo código del cliente: ")
                    pedido_encontrado["codigo_cliente"] = code_cliente
                    print("Código del cliente actualizado.")
                    guardar_pedidos()

                elif opc == "3":
                    fecha = input("Ingrese la nueva fecha: ")
                    pedido_encontrado["fecha_pedido"] = fecha
                    print("Fecha actualizada.")
                    guardar_pedidos()

                elif opc == "4":
                    print("Volviendo a la modificación de pedidos.")
                    break
            else:
                print("Pedido no encontrado.")
        
        elif modi == "no":
            print("Volviendo a la gestión de pedidos...")
            break

        else:
            print("Opción inválida, vuelva a intentarlo.")

def eliminar_pedidos(): #funcion para eliminar pedidos
    code_pedido = input("Ingrese el código del pedido a eliminar: ")
    pedido_encontrado = next((p for p in pedidos if p["codigo_pedido"] == code_pedido), None)

    if pedido_encontrado:   
        for detalle in pedido_encontrado["detalles_pedido"]:
            producto = next((p for p in productos if p["codigo_producto"] == detalle["codigo_producto"]), None)
            if producto:
                producto["cantidad_en_stock"] += detalle["cantidad"]
                
        pedidos.remove(pedido_encontrado)
        guardar_pedidos()
        guardar_productos()
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
#variable de modificacion de pedidos

sub_menu_modi = """
**********************************
1. Cambiar el número de línea
2. Cambiar código del producto
3. Cambiar cantidad
4. Terminar modificaciones
*********************************
"""
#submenu de mdificaciones

def buscar_pedidos(): #funcion para buscar pedidos
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    print(
        """
        ************ BÚSQUEDA DE PEDIDOS ************
        *********************************************
        escoja
        1. buscar por codigo de pedido
        2. buscar por codigo de cliente
        3. buscar por fecha
        4. buscar por producto
        5. volver al menu principal
        *********************************************
        *********************************************
        """
    )
    opcion = input("\nSeleccione una opción: ").strip()
    resultados=[]
    
    if opcion == "1":
        codigo = input("Ingrese el código del pedido: ").strip()
        resultados = [p for p in pedidos if p["codigo_pedido"] == codigo]

    elif opcion == "2":
        cliente = input("Ingrese el código del cliente: ").strip()
        resultados = [p for p in pedidos if p["codigo_cliente"] == cliente]

    elif opcion == "3":
        fecha = input("Ingrese la fecha del pedido (YYYY-MM-DD): ").strip()
        resultados = [p for p in pedidos if p["fecha_pedido"] == fecha]

    elif opcion == "4":
        producto = input("Ingrese el código del producto: ").strip()
        resultados = [p for p in pedidos if any(d["codigo_producto"] == producto for d in p["detalles_pedido"])]

    elif opcion == "5":
        print("Volviendo al menú...")
        return
    else:
        print("Opción inválida. Intente de nuevo.")
        return
    
    if resultados:
        print("\n************ RESULTADOS DE LA BÚSQUEDA ************")
        print("Código       | Cliente     | Fecha        | Total      ")
        print("------------|------------|-------------|------------")
        for p in resultados:
            print(f"{p['codigo_pedido'].ljust(12)} | {p['codigo_cliente'].ljust(10)} | {p['fecha_pedido'].ljust(12)} | ${str(p['total']).ljust(10)}")
        print("***************************************************")
    else:
        print("No se encontraron pedidos con los criterios de búsqueda.")
        