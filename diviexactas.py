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

division=(a/b)
resultado=(a%b)

if resultado==0:
    print(f'{a} y {b} es una division exacta')
else:
    print(f'{a} y {b} es una division inexacta')

print(f'el resultado de la division es: {division}')
