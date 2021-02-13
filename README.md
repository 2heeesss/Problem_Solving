# PS 하면서 알게된것들

## 기본 입출력
- 입력받아야할게 많은경우
input()으로 받아서 시간초과 발생할때 사용
```python
import sys
read =  sys.stdin.readline
n = read().rstrip()
```
- 개행하지않고 출력하기
```python
print(a, end='')
```
 - 출력 사이사이 개행
 ```python
 print(1, 2, 3, sep = '\n')
 ```


---
<br><br>


## 리스트
- 2차원 리스트 만들기
```python
# m, n 주어졌을때 행렬
m, n = 5,4
a = [[0]*m for _ in range(n)]

# n 줄의 행렬 입력받기
a = [list(map(int, input())) for _ in range(n)]
```
- 리스트 슬라이싱
기본구조 a[start : end : step]
1. start: 슬라이싱 시작할 위치
2. end: 슬라이싱을 끝낼위치
3. step: 몇개씩 끊어서 가져올지 정하기
```python
# 기본 예제
a = ['a', 'b', 'c'. 'd', 'e']
a[1:]  # -> ['b', 'c', 'd', 'e']
a[-3:]  # -> ['c', 'd', 'e']
a[2:4]  # -> ['c', 'd']

# 활용법_1
# 1차원 리스트를 n, m의 2차원 리스트로 변환하기
for _ in range(n):
    dp.append(arr[index:index + m])
    index += m
```
- 1부터 탐색하기
```python
for i in range(1, n+1)
```



---
<br><br>

### import math

---
<br><br>


### DFS
재귀 깊이 늘리기
### BFS
- 기본개념


---
<br><br>





## sorted, sort 차이
```python
# sort
# sort는 새로운 객체에 저장을 하는것이 아니라 기존 리스트에 바로 정렬해서 저장
arr.sort()

# sorted
# sorted는 새로운 객체에 정렬된 값을 저장
newArr = sorted(arr, reverse = True)
```

---
<br><br>


## 올림, 내림, 반올림
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


---
<br><br>


## collections.Counter
```python
#사용법
from collection import Counter
arr = [1,1,1,2,3,4]
c = Counter(arr) # 튜플로 반환


# Counter 를 List로 반환하기
Counter(arr).most_common() # 튜플이 아니라 리스트로 반환
Counter(arr).most_common(3) # 인자가 들어가면 n개만 반환함

# Counter의 값 확인방법
arr = [10, 10, 10, 20]
arr = Counter(arr) # -> Counter({10: 3, 20: 1})
print(arr[10]) # -> 3    카운터는 인덱스로 확인하는게 아니라 값으로 확인함
```


# 추가할것들
1. 리스트 맨 앞에 추가하기
2. deque쓰는방법
3. insert쓰는방법