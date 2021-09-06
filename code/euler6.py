sumSquares = 0
squareSum = 0

for num in range(1,101):
    sumSquares += num**2
    squareSum += num
squareSum **= 2

print(squareSum - sumSquares)