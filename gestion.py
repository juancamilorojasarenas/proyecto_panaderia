#import json
#pedido=open("pedidos.json")
#producto=open("productos.json")
#pedir=json.load(pedido)
#product=json.load(producto)
#producto_json = json.dumps(pedido)

pedidos = [] 

def agregar_pedido():
    code_pedido=input("ingrese el codigo del pedido: ")
    code_cliente=input("ingrese el codigo del cliente: ")
    fecha=input("ingrese la fecha del pedido: ")

    detalles_pedido=[]

    pedido = {
    "codigo_pedido": code_pedido,
    "codigo_cliente": code_cliente,
    "fecha_pedido": fecha,
    "detalles_pedido": detalles_pedido
    }

    pedidos.append(pedido)
    print("el pedido fue agrgado exitosamente") 

def detalles_pedido(): 
    code_pedido=input("ingrese el codigo del pedido: ")
    pedido_encontrado=None
    for pedido in pedidos:
        if pedido["codigo_pedido"] == code_pedido:
            pedido_encontrado = pedido
            break
    if pedido_encontrado:
        code_producto=input("ingrese el codigo del producto: ")
        cantidad=int(input("ingrese la cantidad del producto: "))
        precio=int(input("precio: "))
        num_linea=int(input("ingresa el numero de linea del pedido: "))
        detalle = {
        "codigo_pedido": code_pedido,
        "codigo_producto": code_producto,
        "cantidad": cantidad,
        "precio_unidad": precio,
        "numero_linea": num_linea
        }
        pedido_encontrado["detalles_pedido"].append(detalle)
        print("El detalle del pedido fue agregado exitosamente.")
    else: 
        print("el pedido no se ha realizado previamente")
      
def pedir():
    while True:
        continuar=input("desea realizar un pedido(si/no): ").lower()
        if continuar=="si":
            agregar_pedido()
            while True:
                agreg=input ("desea agregar detalles del pedido(si/no): ").lower()
                if agreg=="si":
                    detalles_pedido()
                elif agreg=="no":
                    print("volviendo al menu de gestion de pedidos...")
                    break
                else:
                    print("por favor vuelva a intentarlo")
        elif continuar=="no":
            print("volviendo a la gestion de pedidos...")
            break
        else:
            print("esa opccion no esta disponible intente de nuevo")

def mostrar_pedidos():
    print(pedidos)

def modificar_pedidos():
    while True:
        modi=input("desea modificar un pedido(si/no): ").lower()
        if modi=="si":
            while True:
                code_pedido=input("ingrese el codigo del pedido a modificar: ")
                pedido_encontrado=None
                for pedido in pedidos:
                    if pedido["codigo_pedido"] == code_pedido:
                        pedido_encontrado = pedido
                        break
                if pedido_encontrado:
                    print(modi_pedidos)
                    opc=input("por favor ingrese la opccion que desea modificar")
                    if opc=="1":
                        while True:
                            print(sub_menu_modi)
                            op=input("escoja por favor: ")
                            if op=="1":
                                num_linea=int(input("ingresa el nuevo numero de linea: "))
                                for detalle in pedido_encontrado["detalles_pedido"]:
                                    if detalle["numero_linea"] == num_linea:
                                        detalle["numero_linea"] = num_linea
                                        print(f"El número de línea {num_linea} ha sido actualizado.")
                            elif op=="2":
                                code_producto=input("ingrese el nuevo codigo del producto: ")
                                for detalle in pedido_encontrado["detalles_pedido"]:
                                    if detalle["codigo_producto"] == code_producto:
                                        detalle["codigo_producto"] = code_producto
                                        print(f"El código de producto ha sido actualizado a {code_producto}.")
                            elif op=="3":
                                cantidad=int(input("ingresa la nueva cantidad: "))
                                for detalle in pedido_encontrado["detalles_pedido"]:
                                    if detalle["cantidad"] == cantidad:
                                        detalle["cantidad"] = cantidad
                                        print(f"La cantidad ha sido actualizada a {cantidad}.")
                            elif op=="4":
                                print("terminando modificaciones...")
                                break
                    elif opc=="2":
                        code_cliente=input("ingresa el nuevo codigo del cliente: ")
                        for pedido in pedido_encontrado["codigo_cliente"]:
                             if pedido["codigo_cliente"] == code_cliente:
                                    pedido["codigo_cliente"] = code_cliente
                                    print(f"el codigo del cliente ha sido actualizado {code_cliente}.")
                    elif opc=="3":
                        fecha=input("ingrese la nueva fecha: ")
                        for pedido in pedido_encontrado["fecha_pedido"]:
                             if pedido["fecha_pedido"] == fecha:
                                    pedido["fecha_pedido"] = fecha
                                    print(f"la fecha se ha actualizado {fecha}.")
                    elif opc=="4":
                        print("volviendo a la modificacion de pedidos")
                        break
                    else:
                        print("opcion no valida vuelva a intentarlo")
                else:
                    print("pedido inexistente vuelva a intentarlo: ")
        elif modi=="no":
            print("volviendo a la gestion de pedidos...")    
            break
        else: 
            print("vuelva a intentarlo")        

def eliminar_pedidos():
    code_pedido=input("ingrese el codigo del pedido a eliminar: ")
    pedido_encontrado=None
    for pedido in pedidos:
        if pedido["codigo_pedido"] == code_pedido:
            pedido_encontrado = pedido
            break
    if pedido_encontrado:   
        pedidos.remove(pedido_encontrado)
        print("el pedido fue eliminado exitosamente")  
    else:
        print ("el pedido no existe o ya fue elimnado anteriormente")

modi_pedidos="""
**********************************************
1. editar detalles del pedido
2. editar codigo del cliente
3. editar fecha del pedido
4. volver al menu de gestion de pedidos
**********************************************
"""

sub_menu_modi="""
**********************************
1. cambiar el numero de linea
2. cambiar codigo del producto
3. cambiar cantidad
4. terminar modificaciones
*********************************
"""