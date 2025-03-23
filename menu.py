from registro import registrar, mostrar_productos, eliminar_producto, modificar_producto
from gestion import pedir, mostrar_pedidos, modificar_pedidos, eliminar_pedidos

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
3. buscar productos
4. eliminar productos
5. modificar productos
6. Volver al menu principal
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
4. Eliminar pedidos
5. buscar pedidos
6. Volver al menu principal
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
            registrar()
        elif opc1=="2":
            mostrar_productos()
        elif opc1=="3":
            print("buscar")
        elif opc1=="4":
            eliminar_producto() 
        elif opc1=="5":
            modificar_producto()   
        elif opc1=="6":
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
            mostrar_pedidos()
        elif opc2=="3":
            modificar_pedidos()
        elif opc2=="4":
            eliminar_pedidos()  
        elif opc2=="5":
            print("")
        elif opc2=="6":
            print("Regresando al menu principal...")
            break
        else:
            print("¡¡LA OPCION NO EXISTE POR FAVOR DIGITE UNA OPCCION CORRECTA!!") 