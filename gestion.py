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
                    opc=input("por favor ingrese la opccion que desea modificar")
                    if opc=="1":
                        while True:
                            print(sub_menu_modi)
                            op=input("escoja por favor: ")
                            if op=="1":
                                num_linea=int(input("ingresa el nuevo numero de linea: "))

                            elif op=="2":
                                code_producto=input("ingrese el nuevo codigo del producto: ")
                            elif op=="3":
                                cantidad=int(input("ingresa la nueva cantidad: "))
                            elif op=="4":
                                print("terminando modificaciones...")
                                break
                    elif opc=="2":
                        print("editar codigo cliente")
                    elif opc=="3":
                        print("editar fecha")
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

sub_menu_modi="""
**********************************
1. cambiar el numero de linea
2. cambiar codigo del producto
3. cambiar cantidad
4. terminar modificaciones
*********************************
"""