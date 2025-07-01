# empiezo marcando los rangos donde se tiene que mover los digitos

for i in range(0, 8):
    for j in range(i + 1 , 9):
        for k in range(j + 1, 10):

# creo la lista de combinaciones convirtiendo los numeros a string

            combinaciones = (str(i) + str(j) + str(k))
            print(combinaciones, end=',')


respuesta = input("¿Quieres ver las combinaciones en orden invertido? (s/n) ")
if respuesta == 's':
    print(combinaciones)
