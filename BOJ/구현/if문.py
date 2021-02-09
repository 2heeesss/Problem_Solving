# 9498 - 시험성적
# score = int(input())

# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score <= 89:
#     print('B')
# elif 70 <= score <= 79:
#     print('C')
# elif 60 <= score <= 69:
#     print('D')
# else:
#     print('F')


# 2753 - 윤년
# year = int(input())
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print(1)
# else:
#     print(0)


# 14681 - 사분면고르기
# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)


# 2884 - 알람시계
# h, m = map(int, input().split())

# if m < 45:
#     if h-1 < 0:
#         print(23, m+15)
#     else:
#         print(h-1, m+15)
# else:
#     print(h, m-45)
