# 무엇을 타겟으로 둘지 생각하고 풀자
# 블루레이 안에 들어갈 최소값은 레슨 리스트의 최대값
# 블루레이 안에 들어갈 최대값은 레슨 리스트의 합
# 위 두 값을 start, end로 설정하고 이분탐색
# 인덱스의 처음부터 합한 값이 mid 초과할경우 카운트
# 카운트 한 값이 m(원하는 값)보다 작으면 end를 mid -1 로 바꿔줌

import sys
n, m = list(map(int, sys.stdin.readline().rstrip().split()))
lessonList = list(map(int, sys.stdin.readline().rstrip().split()))

start = max(lessonList)
end = sum(lessonList)


while start <= end:
    mid = (start+end)//2
    cnt = 1
    bluerayLength = 0

    for i in range(n):
        if bluerayLength + lessonList[i] > mid:
            cnt += 1
            bluerayLength = 0
        bluerayLength += lessonList[i]

    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)
