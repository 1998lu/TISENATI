from productos import crearproductos,listaproductos
#l = []
#print(crearproductos(l))
def menu():
    lista_de_productos = []
    omenu=""" 
    supermercado elija la opcion 
             
    1. listar los producto
    2. agregar mas producto_costo
    3. vender producto
    4. salir
    """
    flag = True
    while flag:
        try:
            print(omenu)
            opcion = int(input("elige la opcion: "))
        except ValueError:
            print('has elegido una opcion que no esta en el menu')
            listaproductos(lista_de_productos)

        else:
            if opcion == 1: 
                print("listando productos")
                print(lista_de_productos)
            elif opcion == 2:
                print("agregando mas productos")
                crearproductos(lista_de_productos)
            elif opcion == 4:
                print("saliendo")
                flag = False
menu()
