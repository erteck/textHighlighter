import math
import time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor


def isprime(n):
    """
    Función que recibe un número "n" y regresa dicho número si y solo si este es un
    número primo. En caso de no serlo, la función regresa 0.
    """
    if n < 2:
        return 0
    else:
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n%i == 0:
               return 0
        return n


def main():
    """
    Función que calcula e imprime la suma de todos los números primos menores o iguales a 5,000,000
    haciendo uso de procesos paralelos.
    """
    n = 5000000
    lst = []
    for i in range(1,n+1):
        lst.append(i)
    print('end')
    with ProcessPoolExecutor(max_workers = 6) as executor:
        future = executor.map(isprime,lst,chunksize=900000)
    print('Resultado: '+ str(sum(future)))
    

if __name__ == '__main__':
    startTime = time.time()
    main()
    finishTime = time.time() - startTime
    print('Tiempo Final: '+ str(finishTime))
    
    

