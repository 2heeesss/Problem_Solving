x, y = 1, 1
dx = [0, 0, -1, 0, 1]
dy = [0, -1, 0, 1, 0]
lx = [0, 0, -1, 0, 1]
ly = [0, 1, 0, -1, 0]
move_type = ['D', 'L']
d = 0
l = 0
nx = 0
ny = 0
count_move = 0
# 입력1
n = int(input())
arr = [[0]*n for _ in range(n)]  # 2차원배열 만들기 알아두자
# 입력2
k = int(input())
apple = [0]*k
for i in range(k):
    apple[i] = list(map(int, input().split()))
# 입력3
l = int(input())
sec = [0]*(l+1)
plan = [0]*l
for i in range(l):
    sec[i], plan[i] = input().split()


# 입력받은 문자 숫자로 바꾸기
for j in range(l):
    sec[j] = int(sec[j])

print(sec[0])
print(plan[0])
# max_move = sec[len(sec)-2]
# print('haha', max_move)
#x = x + sec[0]
# r = len(sec)-1

for i in range(l):
    for _ in range(sec[i]):
        if i == 0:
            count_move += 1
            x = x+1
            print(x)
        else:
            if plan[i-1] == 'D':
                d += 1
                d = d % 4
                x = x + dx[d]
                y = y + dy[d]
                print(x, y)
                count_move += 1
            elif plan[i-1] == 'L':
                print(plan[i-1])
                print('3333')
                l += 1
                l = l % 4
                x = x + lx[l]
                y = y + ly[l]
                print(x, y)
                count_move += 1

        if nx < 1 or ny < 1 or nx > n or nx > n:
            print(count_move)
            break
        x, y = nx, ny

print(count_move)
