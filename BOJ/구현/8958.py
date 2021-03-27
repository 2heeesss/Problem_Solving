import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0

while cnt != n:
    quiz = input().rstrip()
    result = [0] * len(quiz)

    if quiz[0] == 'O':
        result[0] = 1
    else:
        result[0] = 0

    for i in range(1, len(quiz)):
        if quiz[i] == 'O':
            result[i] = result[i-1] + 1
        else:
            result[i] = 0

    print(sum(result))
    cnt += 1
