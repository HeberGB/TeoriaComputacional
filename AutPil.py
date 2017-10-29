from random import randint
from os import system
from time import sleep
def auPil(cadena):
    system('cls')
    arch = open('Pila.txt','w+')
    pila = ['Z0']

    i = 0
    indice = 0
    while cadena[i] == '0':
        arch.write(cadena[i:len(cadena)] + '\n')
        arch.write(""" ^
 |
|q|
 |
 v
 """)
        arch.write(''.join(pila))
        arch.write('\ndelta(q,' + '0,' + pila[i] + ')=' + '{(q,X' + pila[i] + ')}\n')
        pila.append('X')
        arch.seek(indice)
        print(arch.read())
        sleep(1)
        system('cls')
        arch.seek(0)
        arch.seek(len(arch.read()))
        indice = arch.tell()
        i += 1
    if cadena [i] != '1':
        arch.write('\nLa cadena no es de ceros y unos\n')
        arch.seek(0)
        print(arch.read())
        arch.close()
        return False
    while cadena[i] == '1':
        try:
            arch.write(cadena[i:len(cadena)] + '\n')
            arch.write(""" ^
 |
|q|
 |
 v
 """)
            arch.write(''.join(pila))
            ultimo = pila.pop()
            arch.write('\ndelta(p,1,' + ultimo + ')=' + '{(p,E)}\n')
            i += 1
            arch.seek(indice)
            print(arch.read())
            sleep(1)
            system('cls')
            arch.seek(0)
            arch.seek(len(arch.read()))
            indice = arch.tell()
            if i >= len(cadena):
                break
        except IndexError:
            arch.write('\n########Cadena rechazada########\n')
            arch.seek(0)
            print(arch.read())
            arch.close()
            return False
    if (i == len(cadena)) & (pila == ['Z0']):

        arch.write('')
        arch.write("""\n ^
 |
|q|
 |
 v
 """)
        arch.write(''.join(pila))
        arch.write('\ndelta(p,E,Z0)=' + '{(f,Z0)}\n')
        arch.write('\n########Cadena aceptada########\n')
        arch.seek(indice)
        print(arch.read())
        sleep(1)
        system('cls')
        arch.seek(0)
        arch.seek(len(arch.read()))
        indice = arch.tell()
        arch.close()
        return True
    else:
        arch.write('\n########Cadena rechazada########\n')
        arch.seek(0)
        print(arch.read())
        arch.close()
        return False
def main():
    s = '0'
    while s != 's':
        s = input("""Que quieres hacer?
    1. Modo manual
    2. Modo automatico
    3. Salir
    Opción """)

        if s == '1':
            cadena = input("Ingresa cadena a evaluar: ")
            print(cadena)
            auPil(cadena)
        if s == '2':
            cadena = []
            for i in range(randint(6, 10)):
                cadena.append('0')
            for j in range(randint(6, 10)):
                cadena.append('1')
            cadena = ''.join(cadena)
            print(cadena)
            auPil(cadena)
        if s == '3':
            s = 's'
main()
system('cls')
