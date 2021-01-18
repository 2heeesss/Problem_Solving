MONEY = [500, 100, 50, 10]
N = int(input())*10

a = N//MONEY[0]
N -= a * MONEY[0]

b = N//MONEY[1]
N -= b * MONEY[1]

c = N//MONEY[2]
N -= c * MONEY[2]

d = N//MONEY[3]
N -= d * MONEY[3]

print(a+b+c+d)
