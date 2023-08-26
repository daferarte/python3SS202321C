def multiplicacion(a,b):
    print(f'la multiplicación de {a} X {b} es igual a {a*b}')
    print(f'Y este resultado es par: {par(a*b)}')

def par(a):
    if a % 2 ==0:
        return True
    else:
        return False   

print('inicia el software')
multiplicacion(3,5)
multiplicacion(6,4)
# print("siguiente")
# multiplicacion(6,8)
