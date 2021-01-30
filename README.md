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

# n * n 행렬 입력받기
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

