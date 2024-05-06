## 검색
## 함수
from random import randint, choice
def seqSearch(ary,fdata):
    pos = -1
    for i in range(len(ary)):
        if (ary[i] == fdata):  # 같다면 pos는 i(위치)로 나옴.
            pos = i
            break
    return pos

## 변수
dataAry = [randint(30,190) for _ in range(10)]
findData = choice(dataAry) 

##메인
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)

if (position != -1):
    print(findData, '는', position, '위치에 있음.')
else:
    print(findData, '는 없어요.')

## 이진 검색
## 함수
from random import randint, choice
def binSearch(ary,fdata):
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end):
        mid = (start + end) //2    # 반으로 나눔 5.5 --> 5
        if (ary[mid] == fdata):
            pos = mid
            break                  # 값을 찾으면 break
        elif (ary[mid] < fdata):
            start = mid + 1
        else:
            end = mid - 1
    return pos

## 변수
dataAry = [randint(30,190) for _ in range(10)]
dataAry.sort()
findData = choice(dataAry)  # 할머니 키
# findData = 77

## 메인
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if (position != -1):
    print(findData, '는', position, '위치에 있음.')
else:
    print(findData, '는 없어요.')

## 성능 확인
## 함수
from random import randint, choice
def binSearch(ary, fdata):
    global count
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end):
        count += 1
        mid = (start + end) // 2     # 반으로 나눔 5.5 --> 5
        if (ary[mid] == fdata):
            pos = mid
            break                   # 값을 찾으면 break
        elif (ary[mid] < fdata):    
            start = mid + 1
        else:
            end = mid - 1
    return pos

## 변수
count = 0
dataAry = [randint(0,100000) for _ in range(100000)]
dataAry.sort()
findData = choice(dataAry) 
# findData = 77

## 메인
print('배열 -->', dataAry[:20])
position = binSearch(dataAry, findData)
if (position != -1):
    print(findData, '는', position, '위치에 있음.(',count,'번 )')
else:
    print(findData, '는 없어요.')

