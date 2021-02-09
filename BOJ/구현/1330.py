a, b = map(int, input().split())
result = 0
if a > b:
    result = '>'
elif a < b:
    result = '<'
else:
    result = '=='

print(result)
