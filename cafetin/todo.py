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
            def menudesayuno():
                menudesayuno = """
                1. cafe.............s/4.50
                2.chocolate.........s/5.00
                3.jugo de fresas....s/9.00
                4.jugo de papaya....s/8.00
                5.pan con pollo.....s/7.00
                6.pan con jamon.....s/7.00
                7.pan con tortilla..s/7.00
                """

        elif opcion == 2:
            print("Categoria Almuerzo")
        elif opcion == 3:
            print("Categoria Cena")                
        elif opcion == 4:
            print("saliendo")
            break

    

