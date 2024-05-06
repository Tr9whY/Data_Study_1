"""
# 정렬
- 중요 알고리즘 중 하나인 정렬(Soft)은 자료들을 일정한 순서대로 나열한 것.
- 선택 정렬 : 여러 데이터 중에서 가장 작은 값을 뽑는 작동을 반복하여 값을 정렬
- 삽입 정렬
- 버블 정렬
- 퀵 정렬
"""

## 최솟값 찾기
## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):  # 비교 하였을 때 최솟값 변수보다 작다면 바꾸어줌.
            minIdx = i
    return minIdx

## 변수
testAry = [55, 88, 33, 77]

## 메인
minPos = findMinIndex(testAry)
print('최솟값 -->', testAry[minPos])

## 함수
from random import randint

def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i] ):
            minIdx = i
    return minIdx

## 변수
before = [randint(30,190) for _ in range(10)]
after = []

## 메인
print('정렬 전 -->', before)
for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])   # 빼쭤야 그 다음 순서대로 정렬.

print('정렬 후-->',after)

### 개선된 선택 정렬 구현.
## 함수
from random import randint
def selectSort(ary):
    n = len(ary)                 # 전체 데이터 개수
    for i in range(0, n-1,1):    # 사이클(큰 회전)
        minIdx = i
        for j in range(i+1, n, 1):       # i+1은 맨 앞의 최솟 값이 정해졌으므로 다음으로 이동.
            if(ary[minIdx] > ary[j]):
                minIdx = j
        ary[i], ary[minIdx] = ary[minIdx],ary[i] # 가장 최솟값으로 자리를 바꿈
    return ary
    
## 변수
dataAry = [randint(30,190) for _ in range(10)]


## 메인

print('정렬 전 -->', dataAry)
dataAry = selectSort(dataAry)
print('정렬 후 -->', dataAry)
