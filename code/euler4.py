numbers = []

def palindrome(n):
    digits = list(str(n))
    midpoint = int(len(digits)/2)
    if len(digits) % 2 == 0:
        front = digits[:midpoint]
        back = digits[midpoint:]
    else:
        front = digits[:midpoint]
        back = digits[midpoint+1:]
    back.reverse()
    return (front,back)

palindrome(9455649)
palindrome(9009)

for i in range(100,999):
    for j in range(100,999):
        num = i*j
        if palindrome(num)[0] == palindrome(num)[1]: numbers.append(num)

print(max(numbers))