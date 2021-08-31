#Los divisores propios de un número n son aquellos divisores positivos menores que n.
#Un número entero positivo n se dice que es perfecto si la suma de sus divisores propios es igual a n.
#Realiza un programa que lea un número y muestre un mensaje indicando si es perfecto o no.

def main():
    #escribe tu código abajo de esta línea
    #numero = int(input('Cuál número: '))
    suma = 0
    i = 1
    j=1

    while j <= 17000:
        numero = j
        while (i<numero):
            if numero%i == 0:
                suma += i
            i = i + 1
        
        if suma == numero:
            print(f'{j} es perfecto')

        j += 1
        suma = 0
        i = 1
if __name__=='__main__':
    main()