from random import randint

def producciones(palindromo, produccion):
    if produccion == 1:
        return
    if produccion == 2:
        palindromo.insert(int(len(palindromo)/2), 0)
    if produccion == 3:
        palindromo.insert(int(len(palindromo)/2), 1)
    if produccion == 4:
        palindromo.insert(int(len(palindromo)/2), 0)
        palindromo.insert(int(len(palindromo)/2), 0)
    if produccion == 5:
        palindromo.insert(int(len(palindromo)/2), 1)
        palindromo.insert(int(len(palindromo)/2), 1)
def main():
    fin = 'n'
    while fin == 'n':
        n = int(input("Ingresa el tamaño del palindromo: "))
        palindromo = []
        produccion = 0
        if n%2 == 0:
            for i in range(int(n/2)):
                if i < (n/2)-1:
                    produccion = randint(4,5)
                    producciones(palindromo, produccion)
                    palindromo.insert(int(len(palindromo)/2), 'P')
                    print(palindromo)
                    palindromo.remove('P')
                else:
                    produccion = randint(4,5)
                    producciones(palindromo, produccion)
                    print(palindromo)

        else:
            for i in range(int(n/2)+1):
                if i < (n/2)-1:
                    produccion = randint(4,5)
                    producciones(palindromo, produccion)
                    palindromo.insert(int(len(palindromo)/2), 'P')
                    print(palindromo)
                    palindromo.remove('P')
                else:
                    produccion = randint(2,3)
                    producciones(palindromo, produccion)
                    print(palindromo)
        fin = input("Quieres salir? [s/n]   ")

main()
