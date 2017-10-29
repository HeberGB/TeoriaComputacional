import random
def multiplicacion (alfabeto, alfabetoPotencia):
    subconjuntos = []
    for i in range(len(alfabetoPotencia)):
        for j in range(len(alfabeto)):
            subconjuntos.append(alfabetoPotencia[i] + alfabeto[j])
    return subconjuntos

def sigmaN (alfabeto, potencia):
    alfabetoPotencia = alfabeto
    n = 1
    while n < potencia:
        n = n + 1
        alfabetoPotencia = multiplicacion(alfabeto, alfabetoPotencia)
    return alfabetoPotencia

def alfabetoRand (tamaño):
        alfabeto = []
        for i in range(tamaño):
            alfabeto.append(chr(random.randrange(33,254)))
        return alfabeto

eleccion = input ("""Escoge una opcion
    #1. Caracteres random
    #2. Caracteres a eleccion\n""")

if eleccion == "1":
    tamaño = int(input("Ingresa el tamaño del alfabeto: "))
    alfabeto = alfabetoRand (tamaño)

if eleccion == "2":
    alfabeto = [x for x in input("Introduce el alfabeto colocando un espacio entre cada caracter\n").split()]

potencia = int(input("Ingresa la potencia: "))
print ("""
    El alfabeto es: """, alfabeto, "\nY sera elevado a: ", potencia)

archivo = open("salida.txt", "w")
for i in range(len(sigmaN(alfabeto, potencia))):
    archivo.write(sigmaN(alfabeto, potencia)[i]+"\n")
archivo.close()
