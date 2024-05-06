"""
## Stack
Push
- 스택에 데이터를 삽입하는 작동

Pop
- 스택에 데이터를 추출하는 작동

Top
- 스택에 들어 있는 가장 위의 데이터 : Top
- top가 -1 이면 초깃값 (스택이 텅 비었다..!)
"""

## 변수
stack = [None,None,None,None,None] # 빈 공간 설정
top = -1 # top 초깃값 설정

#Push
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'

print('바닥 : ',stack)

# Pop
data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)

data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)

data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)

print('팝-->',data)
print('바닥 : ',stack)

## 함수
def isStackFull():  #스택이 꽉 채워졌는지 확인
    global SIZE,stack, top
    if (top == SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE,stack, top
    if (isStackFull()):   #isStackFull == True
        print("스택이 가득 찼습니다.")
        return
    top += 1            # 다음 들어갈 위치 지정
    stack[top] = data
    # 스택이 가득 채워졌는지 확인해야함

def isStackEmpty():  # 스택이 비었는지 확인하는 함수
    global SIZE,stack, top
    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE,stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return
    data = stack[top]
    stack[top] = None   # data변수에 저장하고 해당 인덱스에 있는 값을 None으로 초기화
    top -= 1            # 변수 1을 감소시켜 다음으로 꺼낼 위치를 지정.
    return data

def peek():
    global SIZE,stack, top
    if (isStackEmpty()):
        print("스택이 텅")
        return
    return stack[top]

## 변수
SIZE = 5
stack = [None for _ in range(SIZE)] # SIZE만큼의 반복을 수행하면서 어떠한 작업도 수행하지 않는다는 것을 명시적으로 나타내는 용도로 사용
top = -1

##메인
push('커피')
push('녹차')
"""
push('꿀물')
push('콜라')
push('환타')
print('바닥:', stack)

push('게토레이')
print('바닥:', stack)
"""

retData = pop()
print('팝-->', retData)

print('다음 예정==>', peek())

retData = pop()
print('팝-->', retData)

retData = pop()
print('팝-->', retData)
print('바닥:', stack)
