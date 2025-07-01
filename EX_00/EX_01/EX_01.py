"""

Requisitos funcionales:
El programa debe generar todas las combinaciones de tres dígitos (del 0 al 9) sin repetir dígitos y donde cada combinación cumpla que el primer dígito < segundo dígito < tercer dígito. Ejemplo válido: 027 Ejemplo inválido: 272, 321, 999.

El programa debe preguntar al usuario si desea que las combinaciones se muestren en:

Orden normal (de menor a mayor): 012, 013, 014, ..., 789
Orden invertido (de mayor a menor): 789, 689, 679, ..., 012
El resultado debe mostrarse en pantalla, separado por comas, en una sola línea.

Debe usarse el siguiente prototipo de funciones:

def print_comb(invertido=False):
def main():
El programa debe ejecutarse únicamente cuando se llame directamente desde el terminal, usando:
if __name__ == "__main__":
    main()
Requisitos técnicos:
No se permite usar itertools, set, sorted, sort(), ni funciones similares de ordenación o filtrado automático.
Solo se debe utilizar listas, bucles for, y estructuras de control como if.
El orden invertido debe implementarse manualmente, sin usar [::-1] ni .reverse().
def print_comb(invertido=False):
    # empiezo marcando los rangos donde se tiene que mover los digitos
    combinaciones = []

    for i in range(0, 8):
        for j in range(i + 1, 9):
            for k in range(j + 1, 10):
                # creo la lista de combinaciones convirtiendo los numeros a string
                combinaciones.append(str(i) + str(j) + str(k))

    if invertido:
        combinaciones.reverse()

    print(', '.join(combinaciones))
"""



# empiezo marcando los rangos donde se tiene que mover los digitos dentro de la lista 

combinaciones = []
for i in range(0, 8):
    for j in range(i + 1, 9):
        for k in range(j + 1, 10):
            combinaciones.append(str(i) + str(j) + str(k))


respuesta = input("¿Quieres ver las combinaciones en orden invertido? (s/n) ")
if respuesta == 's':
    combinaciones = combinaciones[::-1]
    print(', '.join(combinaciones))

else:
    print(', '.join(combinaciones))
