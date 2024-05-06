"""
## 재귀 호출
양쪽에 거울이 있을 때 거울에 비친 자신이 무한 반복해서 비치는 것 또는 
마트료시카 인형처럼 동일한 작동을 무한적으로 반복하는 알고리즘
"""

## 함수
def openBox():
    global count
    print('상자를 엽니다.')
    count -= 1
    if (count == 0):
        print('**선물 넣기**')
        return
    openBox()
    print('상자 닫기 ###')

## 메인
count = 10
openBox()

""" 결과 : 
상자를 엽니다.
상자를 엽니다.
상자를 엽니다.
상자를 엽니다.
상자를 엽니다.
상자를 엽니다.
상자를 엽니다.
상자를 엽니다.
상자를 엽니다.
상자를 엽니다.
**선물 넣기**
상자 닫기 ###
상자 닫기 ###
상자 닫기 ###
상자 닫기 ###
상자 닫기 ###
상자 닫기 ###
상자 닫기 ###
상자 닫기 ###
상자 닫기 ###
"""

## 1부터 10까지 합계 구하기
## 함수
def addNumber(num):
    if (num == 1):
        return 1
    return num+addNumber(num-1)

## 변수
print(addNumber(10))

def printStar(n):
    if n > 0:
        printStar(n-1)
        print('*'*n)
printStar(5)

## 팩토리얼
def factorial(num):
    if num <= 1:
        print('1 반환')
        return 1
    print("%d*%d! 호출"%(num,num-1))
    retVal = factorial(num-1)

    print("%d*%d!(=%d) 반환"%(num, num-1, retVal))
    return num* retVal

print('\n5!=',factorial(5))
