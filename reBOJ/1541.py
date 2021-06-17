expression = list(input().split('-'))
result = 0
for i in range(len(expression)):
    if i == 0:
        arr = list(map(int, (expression[i].split('+'))))
        result += sum(arr)
    else:
        arr = list(map(int, (expression[i].split('+'))))
        result -= sum(arr)

print(result)
