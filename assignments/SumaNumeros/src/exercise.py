#Escribe un programa que lea del teclado números enteros y los vaya contando y sumando. El programa se debe detener cuando la suma de los números leídos sea 1000 o más.
#Cuando la suma sea 1000 o más, el programa debe mostrar el total de la suma, y la cantidad de números que se sumaron.

def main():
    #escribe tu código abajo de esta línea
    i = 0
    suma = 0
    
    while suma < 1000:
        num = int(input('Ingresa un número entero: '))
        i+=1
        suma += num
    print(f'''Suma = {suma}
Cantidad de números = {i}''')

if __name__=='__main__':
    main()