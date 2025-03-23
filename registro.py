import json

def cargar_productos():
    try:
        with open("productos.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def guardar_productos():
    if productos:
        with open("productos.json", "w") as file:
            json.dump(productos, file, indent=4)

productos = cargar_productos()

def registrar():
    while True:
        opc=input("desea registrar un producto(si/no): ").lower()
        if opc=="si": 
            code_producto=input("ingrese el codigo del producto a registrar: "
                                )
            if any(p["codigo_producto"] == code_producto for p in productos):
                print("El producto ya existe, intente con otro código.")
                continue

            else:
                nombre_producto=input("ingrese el nombre del producto: ")
                categoria=input("ingrese la categoria del producto: ")
                descripcion= input("ingrese la descripcion de producto: ")   
                proveedor= input("ingrese el nombre del proveedor: ")

                try:
                        stock=int(input("la cantidad de stock del producto: "))
                        precio_venta=int(input("ingrese el precio de venta: "))
                        precio_provedor=int(input("ingrese el precio del provedor: "))

                        if stock < 0 or precio_venta < 0 or precio_provedor < 0:
                            print("Los valores numéricos deben ser positivos.")
                            continue

                except ValueError:
                        print("ingrese solo valores numericos")
                        continue

                producto = {
                    "codigo_producto": code_producto,
                    "nombre": nombre_producto,
                    "categoria": categoria,
                    "descripcion": descripcion,
                    "proveedor": proveedor,
                    "cantidad_en_stock": stock,
                    "precio_venta": precio_venta,
                    "precio_proveedor": precio_provedor
                }
                    
                productos.append(producto)
                guardar_productos()
                print("el producto fue agrgado exitosamente") 

        elif opc=="no":
            print("volviendo al menu de gestion de productos...")
            break
        else:
            print("volve a intentarlo")

def mostrar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("************Inventario de Productos************")
        print("Código  | Nombre         | Stock | Precio Venta")
        print("--------|---------------|-------|-------------")
        for p in productos:
             print(f"{p['codigo_producto'].ljust(9)} | {p['nombre'].ljust(25)} | {str(p['cantidad_en_stock']).ljust(5)} | {p['precio_venta']}")
             
def eliminar_producto():
    code_producto = input("Ingrese el código del producto a eliminar: ")
    producto_encontrado = next((p for p in productos if p["codigo_producto"] == code_producto), None)
    if producto_encontrado:
        productos.remove(producto_encontrado)
        guardar_productos()
        print("El pedido fue eliminado exitosamente.")  
        
    else:
        print("El pedido no existe o ya fue eliminado anteriormente.")       
        
def modificar_producto():
    while True:
        code_producto = input("Ingrese el código del producto a modificar: ")
        producto_encontrado = next((p for p in productos if p["codigo_producto"] == code_producto), None)
        
        if not producto_encontrado:
            print("El producto no existe.")
            return

        print("""
        **************MODIFICAR PRODUCTO****************
        ************************************************
        escoja la opcion
        1. cambiar el nombre 
        2. cambiar la categoria
        3. cambiar la descripcon
        4. cambiar el provedor
        5. cambiar la cantidad en stock
        6. cambiar el precio de venta
        7. cambiar el precio del proveedor
        8. volver al menu principal
        ************************************************
        ************************************************
        """      
    )
        opcion = input("Ingrese la opccion que desea modificar: ")

        if opcion == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            producto_encontrado["nombre"] = nuevo_nombre
        elif opcion == "2":
            nueva_categoria = input("Ingrese la nueva categoría: ")
            producto_encontrado["categoria"] = nueva_categoria
        elif opcion == "3":
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            producto_encontrado["descripcion"] = nueva_descripcion
        elif opcion == "4":
            nuevo_proveedor = input("Ingrese el nuevo proveedor: ")
            producto_encontrado["proveedor"] = nuevo_proveedor
        elif opcion == "5":
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                producto_encontrado["cantidad_en_stock"] = nueva_cantidad
            except ValueError:
                print("Ingrese un número válido.")
                continue
        elif opcion == "6":
            try:
                nuevo_precio_venta = float(input("Ingrese el nuevo precio de venta: "))
                if nuevo_precio_venta < 0:
                    print("El precio no puede ser negativo.")
                    continue
                producto_encontrado["precio_venta"] = nuevo_precio_venta
            except ValueError:
                print("Ingrese un número válido.")
                continue
        elif opcion == "7":
            try:
                nuevo_precio_proveedor = float(input("Ingrese el nuevo precio del proveedor: "))
                if nuevo_precio_proveedor < 0:
                    print("El precio no puede ser negativo.")
                    continue
                producto_encontrado["precio_proveedor"] = nuevo_precio_proveedor
            except ValueError:
                print("Ingrese un número válido.")
                continue
        elif opcion == "8":
            print("Volviendo al menu principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            continue

        guardar_productos()
        print("Producto modificado exitosamente.")   