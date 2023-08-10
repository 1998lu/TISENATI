class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def info(self):
        return f"{self.nombre} {self.precio} {self.cantidad}"
    
p1 = Producto("cafe", "25", "s/4.50")

    
    
    
