#Escribe un programa que lea los valores a y b y muestre todos los números pares que van desde a hasta b incluyendo los límites.
#Supón que siempre a < b.
#Para este ejercicio considera el valor 0 como par.

def main():
    #escribe tu código abajo de esta línea
    a = int(input('Valor inicial: '))
    b = int(input('Valor inicial: '))

    i = a
    while (i<=b):
        if i%2==0:
            print(i)
        i = i+1 #i++

if __name__=='__main__':
    main()
