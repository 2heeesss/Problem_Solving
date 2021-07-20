import sys
input = sys.stdin.readline
trees = {}
cnt = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
        cnt += 1
    else:
        trees[tree] = 1
        cnt += 1
trees = sorted(trees.items(), key=lambda x: x[0])
for i in trees:
    print(i[0], f'{i[1]/cnt*100:.4f}')

# 소수점 형식 맞추는법
# 입력이 끝날때까지 저장하는법
