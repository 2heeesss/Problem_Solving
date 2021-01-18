n, m = map(int, input().split())
# 행이 n 개인 행렬 만들기
matrix_1 = [list(map(int, input())) for _ in range(n)]
matrix_2 = [list(map(int, input())) for _ in range(n)]

count = 0
a = 0

for i in range(n):
    for j in range(m):
        if matrix_1[i][j] == matrix_2[i][j]:
            pass
        else:
            count += 1
            a = matrix_1[i][j]
            for k in range(n):
                # print(matrix_2[i][k])
                matrix_2[k][i] = a

if matrix_1 == matrix_2:
    print(count)
else:
    print(-1)
