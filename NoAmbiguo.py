from random import randint
def anaGram(parentesis):
    arch = open('GramaNoAmb.txt','w+')
    pasos = []
    pasos.append('B')
    for i in range(len(parentesis)):
        if parentesis[i] == '(':
            pasos.insert(i, '(')
            pasos.insert((len(pasos)-1), 'R')
        elif parentesis[i] == ')':
            if 'R' not in pasos:
                arch.write('Parentesis no balanceados\n')
                arch.seek(0)
                print(arch.read())
                return False
            else:
                indice = pasos.index('R')
                pasos.pop(indice)
                pasos.insert(indice, ')')
        else:
            arch.write('No es un parentesis >:|\n')
            arch.seek(0)
            print(arch.read())

        arch.write(''.join(pasos) + '\n')
    if 'R' not in pasos:
        pasos.pop()
        arch.write(''.join(pasos) + '\n')
        arch.write('Parentesis balanceados\n')
    else:
        arch.write('Parentesis no balanceados\n')
    arch.seek(0)
    print(arch.read() + '\n')
    if 'B' not in pasos:
        return True
    else:
        return False

def main():
    s = '0'
    while s != '3':
        s = input('''Que quieres hacer?
1. Modo manual
2. Modo automatico
3. Salir
   Opción ''')
        if s == '1':
            parentesis = input("Ingresa los parentesis: ")
            print(parentesis)
            anaGram(parentesis)
        if s == '2':
            parentesis = []
            parentesis.append('(')
            for i in range(randint(1, 20)):
                if randint(0,1) == 1:
                    parentesis.append('(')
                if randint(0,1) == 0:
                    parentesis.append(')')
            parentesis = ''.join(parentesis)
            print(parentesis)
            anaGram(parentesis)
main()
