import math
from concurrent.futures import ProcessPoolExecutor
n = 5000000
def isprime(n):
    if n < 2:
        return 0
    elif n == 2:
        return n
    else:
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if n%i == 0:
                return 0
        return n

def main():
    result = 0
    numbers = range (1, n+1)
    with ProcessPoolExecutor(max_workers = 4) as executor:
        results = executor.map(isprime, numbers, chunksize = 1250000) 
    for x in results:
        result += x
    print(result)

if __name__ == '__main__':
    main() 
