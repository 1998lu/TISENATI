class Producto:
    def __init__(self, nombre, marca, precio, cantidad):
        self._nombre = nombre
        self._marca = marca
        self._precio = precio
        self._cantidad = cantidad
    
    def get_nombre(self):
        return self._nombre
