a, b = input().split()
result = [0]*(len(b)-len(a)+1)
for i in range(len(b)-len(a)+1):
    for j in range(len(a)):
        if a[j] == b[j]:
            result[i] += 1
    a = 'F' + a
print(len(b) - (max(result)+len(result)-1))

# 풀이 생각못함
