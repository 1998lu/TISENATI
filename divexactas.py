bandera1=True
bandera2=True
while bandera1:
    try:
        a = int(input("valor 1: "))
        bandera1=False
    except ValueError:
        print("te equivocaste")


while bandera2:
    try:
        b = int(input("valor 2: "))
        bandera2=False
    except ValueError:
        print("te equivocaste")


if(a%b)==0:
    print(f'{a} y {b} es una division exacta')
else:
    print(f'{a} y {b} es una division inexacta')
