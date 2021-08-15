num = 600851475143

def isPrime(n):
    for i in range(2,int(n/2)):
        if n%i == 0:
            return 0
    return 1

for i in range(2, int(num/2)+1):
    if num%i == 0 and isPrime(num/i):
        print(int(num/i))
        break