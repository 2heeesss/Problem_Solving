# 셀프넘버 출력 10000 이하
# 삭제하기 arr.remove('lee')
# 없는것 삭제못함


def notSelfNum(n):
    if 1 <= n <= 9:
        one = n
        return n + one
    elif 10 <= n <= 99:
        one = n % 10
        ten = (n//10) % 10
        return n + one + ten
    elif 100 <= n <= 999:
        one = n % 10
        ten = (n//10) % 10
        hun = n//100
        return n + one + ten + hun
    elif 1000 <= n <= 9999:
        one = n % 10
        ten = (n//10) % 10
        hun = (n//100) % 10
        tho = n//1000
        return n + one + ten + hun + tho


nums = []
n = []
for i in range(1, 10000):
    n.append(notSelfNum(i))
s = set(n)

for i in range(1, 10000):
    nums.append(i)

selfNum = [x for x in nums if x not in s]

for number in selfNum:
    print(number)
