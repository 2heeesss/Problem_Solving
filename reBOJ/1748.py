n = int(input())

i = 1
tens = 1
sum = 0
result = 0

while True:
    if n < 10:
        print(n)
        break
    result += tens*9*i
    sum += tens*9
    i += 1
    tens *= 10
    if n < sum+tens*9:
        result += (n-sum)*i
        print(result)
        break
