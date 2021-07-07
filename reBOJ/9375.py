import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cloth = {}
    result = 1
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if b in cloth.keys():
            cloth[b] += 1
        else:
            cloth[b] = 2

    for i in cloth.values():
        result *= (i)
    print(result - 1)
