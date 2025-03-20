#import json
#pedido=open("pedidos.json")
#producto=open("productos.json")
#pedir=json.load(pedido)
#product=json.load(producto)
#producto_json = json.dumps(pedido)

#pedidos = [] 
    # def agregar_pedido():
    # code_pedido=input("ingrese el codigo del pedido: ")
    # code_cliente=input("ingrese el codigo del cliente: ")
    # fecha=input("ingrese la fecha del pedido: ")
    # pedido = {
    # "codigo_pedido": code_pedido,
    # "codigo_cliente": code_cliente,
    # "fecha_pedido": fecha,
    # "detales_pedido": []
    # }
    # pedidos.append(pedido)
    # print("el pedido fue agrgado exitosamente") 

def detalles_pedido(): 
     code_pedido=input("ingrese el codigo del pedido: ")
     code_producto=input("ingrese el codigo del cliente: ")
     cantidad=int(input("ingrese la cantidad del produccto: "))
     precio=int(input("precio: "))
     detalle = {
     "codigo_pedido": code_pedido,
     "codigo_producto": code_producto,
     "cantidad": cantidad,
     "precio_unidad": precio,
     "numero_linea": len(code_pedido["detalles_pedido"]) + 1
     }
      
def pedir():
    while True:
        continuar=input("desea realizar un pedido: ").lower()
        if continuar=="si":
            print("gg")
        elif continuar=="no":
            print("volviendo a la gestion de pedidos...")
            break
        else:
            print("esa opccion no esta disponible intente de nuevo")