from producto import Producto, input_int
prueba = Producto("LAPTOP", "ASUS", 10000, 21)
lista_producto =[]
lista_producto.append(prueba)

#p = Producto("laptop", "asus", 2000, 5)
#lista_producto.append(p)
#print(lista_producto)
#producto = lista_producto[0]
#print(producto.info())
def comparar_producto(np, mp, list_product):
    existe = False
    for p in list_product:
        if np.upper() == p.get_nombre().upper() and mp.upper() == p.get_marca().upper():
            print("este producto ya existe")
            existe = True
        else:
            print("agregando producto")
    return existe  #para saber si existe o no existe

comparar_producto("laptop", "asus", lista_producto)

def crear_producto(list_product):
    nombre_p = input("nombre del producto: ")
    marca_p = input("marca del producto: ")
    precio_p = input_int("precio del producto: ", "no ingresaste bien el precio")
    cantidad_p = input_int("cantidad del producto: ", "no ingresaste bien la cantidad")

    existencia = comparar_producto(nombre_p,marca_p, lista_producto)   
    if not existencia:
        nuevo_producto = Producto(nombre_p, marca_p, precio_p, cantidad_p)
        list_product.append(nuevo_producto)

#crear_producto(lista_producto)
print(lista_producto)

def listar_producto(list_product):
    c = 0
    for p in list_product:
        c += 1
        print(f"{c}. {p.get_info_nombre()}")
lista_producto(listar_producto)

#print(t.info())

#lista_producto.append(t)
