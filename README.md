# PS 하면서 알게된것들

### 입력
- 입력받아야할게 많은경우
input()으로 받아서 시간초과 발생할때 사용한다
```python
import sys
read =  sys.stdin.readline()
print(read)
```

### 출력
- 개행하지않고 출력하기
```python
print(a, end='')
```
### 1차원 리스트 만들기

### 2차원 리스트 만들기
```python
# m, n 주어졌을때 행렬
m, n = 5,4
a = [[0]*m for _ in range(n)]

# n 줄의 행렬 입력받기
a = [list(map(int, input())) for _ in range(n)]
```
### DFS
재귀 깊이 늘리기
### BFS
- 기본개념


### 1,1 부터 탐색하기
```python
for i in range(1, n+1)
```
리스트 맨 앞에 추가하기
deque쓰는방법
insert쓰는방법

### sorted, sort 차이
```python
# sort
# sort는 새로운 객체에 저장을 하는것이 아니라 기존 리스트에 바로 정렬해서 저장
arr.sort()

# sorted
# sorted는 새로운 객체에 정렬된 값을 저장
newArr = sorted(arr, reverse = True)
```


### 올림, 내림, 반올림
```python
#올림
import math
math.ceil(-3.14) # -> 3
math.ceil(3.14) # -> 4


#내림
import math
math.floor(-3.14) # -> -4
math.floor(3.14) # -> 3

math.trunc(-3.14) # -> -3    trunc()함수는 floor()과는 달리 소수점 아래는 버리고 int형으로 반환함


#반올림
round(3.14) # -> 3
round(3.1415, 2) # -> 3.14    뒤에오는 인자는 소수점 3째자리에서 반올림
round(31.415, -1) # -> 30.0    음수도 사용가능
```