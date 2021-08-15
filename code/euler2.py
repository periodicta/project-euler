def fibonacci(n):
    if n > 1:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return 1

count = 1
sum = 0
while fibonacci(count) <= 4000000:
    if fibonacci(count) % 2 == 0:
        sum += fibonacci(count)
    count+=1

print(sum)