"""
    Actividad 5.2.1 Programación paralela y concurrente en Python
    Edna Jacqueline Zavala Ortega A01750480
    Erick Alberto Bustos Cruz A01378966
"""
import math
import time

def isPrime(n):
    """
    Función que recibe un número "n" y regresa verdadero si y solo si este es un
    número primo. En caso de no serlo, la función regresa falso.
    """
    if n < 2:
        return False
    elif n == 2:
        return n
    else:
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

def main():
    """
    Función que calcula e imprime la suma de todos los números primos menores o iguales a 5,000,000
    de manera secuencial.
    """
    n = 5000000
    result = 0        
    for i in range (1, n+1):
        if isPrime(i):
            result += i
    print('Resultado: '+ str(result))

# Se llama a la función main y se calcula el tiempo que tarda en ejecutarse    
startTime = time.time()
main()
finishTime = time.time() - startTime
print('Tiempo Final: '+ str(finishTime))