from random import randint
def expresionR():
    if randint(0, 10) == 1:
        exp.append('0')
        if randint(0, 10) == 0:
            exp.append('1')
        elif randint(0, 10) == 1:
            exp.append('')
        else:
            exp.append(expresionR())

    else:
        exp.append('10')
        if randint(0, 10) == 1:
            exp.append('')
        elif randint(0, 10) == 1:
            exp.append('1')
        else:
            exp.append(expresionR())

archivo = open('Cadenas.txt', 'w')
archivo.close()

s = '0'
while s != 'n':
    for i in range(10):
        archivo = open('Cadenas.txt', 'a+')
        exp = []
        expresionR()
        exp = list(filter(lambda x: x != None, exp))
        archivo.write(''.join(exp)+'\n')
    num = archivo.tell()
    archivo.seek(0)
    print(archivo.read())
    archivo.seek(num)
    s = input("Quieres generar otras 10 cadenas? [s/n] ")
archivo.seek(0)
print(archivo.read())
archivo.close()
