from math import gcd


def lcm(x, y):
    return x*y//gcd(x, y)


x, y = map(int, input().split())
print(gcd(x, y), lcm(x, y), sep='\n')
