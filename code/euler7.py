prime = 0
num = 2

def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return 0
    return 1

while True:
    if isPrime(num) == 1:
        prime += 1
        if prime == 10001: break
    num += 1

print(num)