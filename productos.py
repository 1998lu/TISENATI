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
            producto= {}
            pregunta=input("desea a gregar mas productos? si/no")
            if str(pregunta) != "si":
                break

            print(lista_productos)

    return lista_productos
#l= [[{'nombre': 'asus', 'marca': 'jjjjj', 'costo': 50, 'cantidad': 5}]]
#crearproductos(l)
#print(l)
#print(crearproductos(lp))
def listaproductos(lista_productos): 
    print('nombre|marca|costo|cantidad')
    for producto in lista_productos:
        print(f'{producto.get("nombre")}|{producto.get("marca")}|{producto.get("costo")}|{producto.get("cantidad")}')
