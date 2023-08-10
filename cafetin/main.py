from producto import listadesayuno
menu = """
CAFETIN-SENATI
Opciones:
1. Desayuno
2. Almuerzo
3. Cena
4. Salir
"""
while True:
    try:
        print(menu)
        opcion= int(input("eliga una opcion: "))
    except ValueError:
        print('has elegido una opcion que no esta en el menu')
    else:
        if opcion == 1: 
            print("Categoria Desayunos")
            print(listadesayuno)
        elif opcion == 2:
            print("Categoria Almuerzo")
        elif opcion == 3:
            print("Categoria Cena")                
        elif opcion == 4:
            print("saliendo")
            break
