class Producto:
    def __init__(self, nombre, marca, precio, cantidad):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad
    
    def info(self):
        return f"{self.nombre} {self.marca} {self.precio} {self.cantidad}"
    
    def actualizar_cantidad(self,cantidad_vendida):
        self.cantidad = self.cantidad - cantidad_vendida
    
    def get_nombre(self):
        return self.nombre
    def get_marca(self):
        return self.marca
    def get_info_completa(self):
        return f"{self.nombre} {self.marca} {self.precio} { self.cantidad}"


p= Producto("teclado", "HP", 50, 300)
i= Producto("laptop", "HP", 2000, 300)

#print(p.info())
#print(i.info())
#p.actualizar_cantidad(20)
#print(p.info())

def input_int(mensaje, mensaje_error): # pide un mensaje
   while True:
        try:
            v = int(input(mensaje))
        except ValueError:
            print(mensaje_error)
            pass
        else:
            return v
