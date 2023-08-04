#productos =[]
#lista para coleccionar elementos-  datos
#productos.append("laptop")
#productos.append("mouse")
#para agregar un elemento mas
#print(productos[1])

#producto = {}
#diccionario - tiene dos valores una clave y un valor
#producto ["nombre"] = "laptop"
#producto ["precio"] = 1200
#print(producto.get("nombre"))
#para seleccionar una clave del diccionario

#productos=[
    #{"producto": 
     #[]}
#]
#se puede tener una lista con un diccionario adentro con una lista dentro del diccionario 
#productos = [1,2,3,4,5,6,7,8]
#suma_elementos = []
#print(productos[0] + 1)
#pARA ITERAR - for y while
#for es un bucle definido deacuerdo a la cantidad de datos de la lista, solo para listas
#for producto in productos:   #o for p in productos:
    #print (producto + 1 )
    #suma_elementos.append(producto + 1)
#print(suma_elementos)
#print(productos)

#print(len(productos))
#cantidad de elementos en una lista
#contador = 0
#while True:
    #while bucle infinito con bandera abierta, cilco infinito que se puede cortar con break o con una bandera a bajo. para ciclos indeterminados
    #print(productos[contador])
    #if (len (productos)-1) == contador: # o if 7 == contador:
        #break
    #else:
        #contador += 1 

#def multiplicacion(numero1, numero2): 
#multiplicacion es el nombre de la funcion. dentro del parentesis se ponen los parametros 
    #resulatado = numero1 * numero2
    #print(resulatado)
    #return resulatado
#return es para q regrese o retorne algo
#print(multiplicacion(5,125))
#valor1 = 12
#valor2 = 2 
#multiplicacion(valor1, valor2) #esta funcion es dinamica, se pueden reemplazar con distintos datos q se estan mandando
#import math

#def area_circunferencia(radio):
    #resultado = 2*math.pi * (radio*radio)
    #print(resultado)

#area_circunferencia(50)


def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

def input_int(mensaje, mensaje_error): # pide un mensaje
   while True:
        try:
            v = int(input(mensaje))
        except ValueError:
            print(mensaje_error)
            pass
        else:
            return v
        
    
    # primero me pide un mensaje entra un while el mensaje lo pide en un input, si ponesmos una lentra no hace nada cuando ponga un numero retorna a un v

#input_int ("escribe un numero: ")


menu = """ 
calculadora
opciones: 
1. sumar
2. restar
3. multiplicar
4. dividir
5. salir
"""
while True:
    print(menu)
    opcion = input_int("elige la opcion: ", "esa opcion es incorrecta") 

    if opcion in [1,2,3,4]:  #si mi opcion esta en [] entonces cerrar el ciclo con break
        a = input_int("ingrese el primer valor: ","no es un numero")
        b = input_int("ingrese el segundo valor: ","no es un numero")
        if opcion == 1:
            print(f"el resultado es {suma(a,b)}")
        elif opcion ==2:
            print(f"el resultado es {resta(a,b)}")
        elif opcion == 3:
            print(f"el resultado es {multiplicacion(a,b)}")
        elif opcion == 4:
            print(f"el resultado es {division(a,b)}")
    elif opcion == 5:
        print ("saliendo")
        break
    else: 
        print("no existe esa opcion")  #entonces imprimir " "
