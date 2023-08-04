from producto import Producto, input_int

lista_producto =[]

p = Producto("laptop", "asus", 2000, 5)
#lista_producto.append(p)
#print(lista_producto)
#producto = lista_producto[0]
#print(producto.info())

nombre_p = input("nombre del producto: ")
marca_p = input("marca del producto: ")
precio_p = input_int("precio del producto: ", "no ingresaste bien el precio")
cantidad_p = input_int("cantidad del producto: ", "no ingresaste bien la cantidad")

t = Producto(nombre_p, marca_p, precio_p, cantidad_p)
print(t.info())

lista_producto.append(t)
