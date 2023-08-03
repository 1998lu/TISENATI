#edad
#color
#tipo_pelaje
#Genero 
#nombre

#accion
#_comer
#_correr
#_dormir
#_sonido

#class gato: 
    #def __init__(self, nombre, genero, color, edad):
        #self._nombre = nombre
        #self._genero = genero
        #self._color = color
        #self._edad = edad 
    
    #def correr(self, punto_llegada):
        #print(f"{self._nombre} tienes que ir a {punto_llegada}")
        #print("si llegaste detente ahi")

    #def dormir(self, tiempo_dormir):
        #print(f"{self._nombre} empieza a dormir {tiempo_dormir}")    

#chimi = gato("chimi","macho","gris",1)
#chimi.correr("a la mesa")

#kitty = gato("kitty","hembra","blanco",1)
#kitty.dormir("15 minutos")

class Persona:
    def __init__(self, nombre, genero, dni, fecha_nacimiento, talla, peso):
        self._nombre = nombre
        self._genero = genero
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento
        self._talla = talla
        self._peso = peso
    def caminar(self, punto_de_llegada):
        print(f"{self._nombre} ve a {punto_de_llegada}")
        print("llegaste XD")
    
    def comer(self,tipo_comida):
        print(f"{self._nombre} ve a comer {tipo_comida}")
        print("¿esta rico verdad?")
    
    def edad(self):
        return 15

p1 = Persona("jose", "varon","01234567", "25/07/1998", "1.75", "80")
p1.caminar("al patio")

p2= Persona("lucero","mujer","52525252", "21/06/2000", "1.55", "55")
p2.comer( "tu sopa")

class Alumno(Persona):
    def __init__(self, nombre, genero, dni, fecha_nacimiento, talla, peso, id_studiante, correo):
        super().__init__(nombre, genero,dni, fecha_nacimiento, talla, peso)
        self._id_estudiante = id_studiante
        self._correo = correo

    def info(self):
        print(f"{self._nombre} {self._dni} {self._id_estudiante}")


juan = Alumno("juan","varon","70825469","05/01/1960", "1.80", "85", "1542725","jxjxjxj@senati.pe")
juan.info()
