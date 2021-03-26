import sys
input = sys.stdin.readline

multipleNum = 1
for _ in range(3):
    multipleNum *= int(input().rstrip())
multipleNum = str(multipleNum)
arr = []
result = [0]*10
for i in range(len(multipleNum)):
    arr.append(int(multipleNum[i]))


for nums in arr:
    for j in range(10):
        if nums == j:
            result[j] += 1
for i in range(10):
    print(result[i])
