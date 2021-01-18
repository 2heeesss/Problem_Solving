# 1000
# A, B = map(int, input().split())
# print(A+B)


# 2558
# A = int(input())
# B = int(input())
# print(A+B)


# 10950
# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     print(A + B)


# 10951
# while True:
#     try:
#         A, B = map(int,input().split())
#         print(sum((A,B)))
#     except:
#         break


# 10952
# while True:
#     A, B = map(int, input().split())
#     if not A and not B:
#         break
#     print(A+B)


# 10953
# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split(','))
#     print(a+b)


# 11021
# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     print(f"Case #{i+1}: {a+b}")


# 11022
# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     print(f"Case #{i+1}: {a} + {b} = {a+b}")


# 11718
# while True:
#     try:
#         a = input()
#         if a[0] == ' ' or a[-1] == ' ':
#             break
#         else:
#             print(a)
#     except:
#         break


# 11719 출력초과
# while True:
#     try:
#         a = sys.stdin.readline().rstrip()
#         print(a)
#     except EOFError:
#         break
# 바꾼답
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break


# 11720 __ 틀림_ 리스트 자료형 파악하고 있을것
# n = int(input())
# a = list(input())
# sum = 0
# for i in range(n):
#     sum += int(a[i])
# print(sum)


# 11721 __ 틀림 _ for문 파악하고있자
# a = input()
# j = 0
# for i in a:
#     print(i, end='')
#     if j % 10 == 9:
#         print()
#     j += 1


# 2741
# n = int(input())
# for i in range(n):
#     i += 1
#     print(i)


# 2742
# n = int(input())
# for i in range(n):
#     print(n-i)


# 2739
# n = int(input())
# for i in range(1, 10):
#     print(f"{n} * {i} = {n*i}")


# 1924
# DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# DAYS_OF_WEEK = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# mon, day = map(int, input().split())

# val = 0
# for i in range(mon-1):
#     val += DAYS[i]
# val += day
# if val % 7 == 0:
#     print(DAYS_OF_WEEK[0])
# elif val % 7 == 1:
#     print(DAYS_OF_WEEK[1])
# elif val % 7 == 2:
#     print(DAYS_OF_WEEK[2])
# elif val % 7 == 3:
#     print(DAYS_OF_WEEK[3])
# elif val % 7 == 4:
#     print(DAYS_OF_WEEK[4])
# elif val % 7 == 5:
#     print(DAYS_OF_WEEK[5])
# else:
#     print(DAYS_OF_WEEK[6])


# 8393
# n = int(input())
# sum = 0
# for i in range(n):
#     sum += (i+1)
# print(sum)


# 10818
# n = int(input())
# arr2 = list(map(int, input().split()))
# arr = [arr2[i] for i in range(n)]
# print(min(arr), max(arr))


# 2438
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     print()


# 2439
# n = int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ', end='')
#     for k in range(i+1):
#         print('*', end='')
#     print()


# 2440
# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print('*', end='')
#     print()


# 2441
# n = int(input())
# for i in range(n):
#     for k in range(i):
#         print(' ', end='')
#     for j in range(n-i):
#         print('*', end='')
#     print()


# 2442
# n = int(input())
# for i in range(n):
#     for _ in range(n-i-1):
#         print(' ', end='')
#     for j in range(2*i+1):
#         print('*', end='')
#     print()


# 2445
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     for _ in range((2*n)-((j+1)*2)):
#         print(' ', end='')
#     for _ in range(i+1):
#         print('*', end='')
#     print()
# for i in range(n-1):
#     for j in range(n-i-1):
#         print('*', end='')
#     for _ in range(2*(i+1)):
#         print(' ', end='')
#     for j in range(n-i-1):
#         print('*', end='')
#     print()


# 2522
# n = int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ', end='')
#     for _ in range(i+1):
#         print('*', end='')
#     print(' ')
# for i in range(n-1):
#     for _ in range(i+1):
#         print(' ', end='')
#     for _ in range(n-i-1):
#         print('*', end='')
#     print(' ')


# 2446
# n = int(input())
# for i in range(n):
#     print(" "*i, end='')
#     print("*"*(n*2-(2*i)-1), end='')
#     print()
# for i in range(n-1):
#     print(" "*(n-i-2), end='')
#     print('*'*(2*i+3), end='')
#     print()


# 10991
# n = int(input())
# for i in range(n):
#     for k in range(n-i-1):
#         print(" ", end='')
#     for j in range(i+1):
#         print('*', end=' ')
#     print()


# 10992
n = int(input())
for i in range(n-1):
    print(' '*(n-i-1), end='')
    print('*', end=' '*(2*i-1))
    if i == 0:
        print()
    else:
        print('*')
print('*'*(2*n-1))
