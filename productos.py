def crearproductos(lista_productos):
    producto = {}
    #bandera=True
    while True:
        try:
            producto_nombre =input("ingrese el nombre del producto: ")
            producto_marca=input("ingrese la marca del producto: ")
            producto_costo=int(input("ingrese el costo del producto: "))
            producto_cantidad=int(input("ingrese la cantidad del producto: "))
            #print("desea agregar mas productos? si/no")
        except ValueError:
            print("algo salio mal intentalo otra vez")
        else:
            producto["nombre"]=producto_nombre
            producto["marca"]=producto_marca
            producto["costo"]=producto_costo
            producto["cantidad"]=producto_cantidad
            lista_productos.append(producto)
            flag_repeticion = coincidenciaproducto(producto_nombre, producto_cantidad, lista_productos)
            if not flag_repeticion:
                lista_productos.append(producto)
            producto= {}
            pregunta=input("desea a gregar mas productos? si/no")
            if str(pregunta) != "SI":
                break

            print(lista_productos)

    return lista_productos
#l= [[{'nombre': 'asus', 'marca': 'jjjjj', 'costo': 50, 'cantidad': 5}]]
#crearproductos(l)
#print(l)
#print(crearproductos(lp))
def listaproductos(lista_productos): 
    print('N° | producto | cantidad | precio')
    counter = 0
    for producto in lista_productos:
        counter += 1
        print(f"{producto.get('nombre')} | {producto.get('costo')} | {producto.get('cantidad')}")

def numerosdenetrada(mensaje): 
    while True:
        try:
            numero_ingreso = int(input(mensaje))
        except ValueError:
            print("te equivocaste esto debe ser un numero")
        else:
            break
    return numero_ingreso

numerosdenetrada("dsfsdfsdfsfsdfsd")

def coincidenciaproducto(producto_nombre, producto_cantidad, lista_productos): 
    #agrega la cantidad de producto registrada
    flag = False
    for producto in lista_productos:
        if producto.get("nombre") == producto_nombre:
            print("este producto ya esta registrado")
            producto["cantidad"] = producto.get('cantidad') + producto_cantidad
            flag = True
    return flag

def venta_productos(lista_de_productos):
    lista_venta = []
    producto_venta = {}
    listaproductos(lista_de_productos)
    while True:
        try:
            seleccionproducto = int(input('elija el numero del producto: '))
            producto = lista_de_productos[seleccionproducto-1]
            producto_cantidad = int(input(f'escriba cantidad de {producto.get("nombre")}: '))
           
        except ValueError:
            print("algo salio mal")
        else:
        
            producto["cantidad"] = producto.get("cantidad") - producto_cantidad
            producto_venta["producto"] = producto.get("nombre")
            producto_venta["cantidad"] = producto_cantidad
            producto_venta["subtotal"] = producto_cantidad * producto.get("costo")
            lista_venta.append(producto_venta)
            listaproductos(lista_de_productos)

            producto_venta = {}
            print(lista_venta)

            pregunta=input("desea a comprar mas productos? si/no")
            if str(pregunta) != "SI":
                break
tarea hacer que al vender un producto no se pueda vender otra vez el prodcuto si ya lo cambio y que aparesca que ya no hay stock si se acabron las unidades 
