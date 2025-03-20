from gestion import pedir

menu_principal= """
************Bienvenid@ a la Panaderia delicias caceras*************
*******************************************************************
Por favor escoja la opcion deseada
1. Gestionar productos
2. Gestionar pedidos
3. Salir del programa
*******************************************************************
*******************************************************************
"""

menu_productos="""
***************Bienvenid@ a la Gestión de productos****************
*******************************************************************
Por favor escoja la opcion deseada
1. Registrar productos
2. Ver inventario
3. Volver al menu principal
*******************************************************************
*******************************************************************
"""

menu_pedidos="""
***************Bienvenid@ a la Gestión de pedidos******************
*******************************************************************
Por favor escoja la opcion deseada
1. Realizar un pedido
2. Ver pedidos
3. Modificar pedidos
4. Volver al menu principal
*******************************************************************
*******************************************************************
"""

def menu():
    while True:
        print(menu_principal)
        opc=input("por favor ingrese su opccion: ")
        if opc=="1":
            opcion_productos()
        elif opc=="2":
            opcion_pedidos()
        elif opc=="3":
            print("Hasta luego...")
            break
        else:
            print("¡¡LA OPCION NO EXISTE POR FAVOR DIGITE UNA OPCCION CORRECTA!!")

def opcion_productos():
    while True:
        print (menu_productos)
        opc1=input("Ingrese la opcion deseada: ")    
        if opc1=="1":
            print("resgistro")
        elif opc1=="2":
            print("inventario")
        elif opc1=="3":
            print("Regresando al menu principal...")
            break
        else:
            print("¡¡LA OPCION NO EXISTE POR FAVOR DIGITE UNA OPCCION CORRECTA!!")       
        
def opcion_pedidos():
    while True:
        print (menu_pedidos)
        opc2=input("Ingrese la opcion deseada: ")    
        if opc2=="1":
            pedir()
        elif opc2=="2":
            print("pedidos")
        elif opc2=="3":
            print("modificando pedidos")
        elif opc2=="4":
            print("Regresando al menu principal...")
            break
        else:
            print("¡¡LA OPCION NO EXISTE POR FAVOR DIGITE UNA OPCCION CORRECTA!!") 
