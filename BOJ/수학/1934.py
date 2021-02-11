import sys

# 최대공약수
# 유클리드 호제법 활용


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


# 최소공배수
def lcm(x, y):
    return x*y // gcd(x, y)

# n 개의 수에 대한 최소공배수
# def overLcm(arr):
#     while True:
#         arr.append(lcm(arr.pop(), arr.pop()))
#         if len(arr) == 1:
#             return arr[0]


# print(overLcm([2, 6, 8, 14]))

read = sys.stdin.readline
t = int(read())
arr = [list(map(int, read().split())) for _ in range(t)]

for i in range(t):
    print(lcm(arr[i][0], arr[i][1]))
