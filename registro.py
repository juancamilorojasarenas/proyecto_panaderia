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
                            print("Error: Los valores numéricos deben ser positivos.")
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
        
                  