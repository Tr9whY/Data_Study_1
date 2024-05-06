"""
# Queue
- 기차가 터널에 들어가는 순서대로 터널을 빠져나오고, ATM기에서 줄을 선 순서대로 예금을 인출하는 것처럼 큐는 먼저 들어간 것이 먼저 나오는 구조를 의미
- Queue 자료 구조는 입구와 출구가 따로 있는 원통 형태
"""

"""
enQueue : 큐에 데이터를 삽입하는 작동
deQueue : 데이터를 추출하는 작동
front : 저장된 데이터 중 첫 번째 데이터
rear : 저장된 데이터 중 마지막 데이터
"""

# Queue 기본 작동 원리
## 변수
SIZE = 5     # 크기 생성
queue = [None for _ in range(SIZE)]
front = rear = -1 # 초기화

## enQueue()
rear += 1   
queue[rear] = '아이네'
rear += 1
queue[rear] = '징버거'
rear += 1
queue[rear] = '릴파'
print('출구 <--', queue,'<--입구')

""" 결과 :
출구 <-- ['아이네', '징버거', '릴파', None, None] <--입구
"""

## deQueue()
front += 1
data = queue[front]
queue[front] = None
print('식사손님 ==>',data)

front += 1
data = queue[front]
queue[front] = None
print('식사손님 ==>',data)

front += 1
data = queue[front]
queue[front] = None
print('식사손님 ==>',data)

print('출구 <--', queue, '<--입구')

"""결과 :
식사손님 ==> 아이네
식사손님 ==> 징버거
식사손님 ==> 릴파
출구 <-- [None, None, None, None, None] <--입구
"""

## 함수
def isQueueFull():
    global SIZE, queue,front,rear
    if (rear >= SIZE-1):   # >= 혹시나 하는 안전상 이유로 씀
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 꽉찼다.")
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):  # head rear가 같은지 확인
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 텅 비었다.")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 텅 비었다.")
        return
    return queue[front+1]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1 # 초기화

## 메인
enQueue('아이네')
enQueue('징버거')
enQueue('릴파')
enQueue('주르르')
enQueue('비챤')
print('출구 <--', queue, '<-- 입구')   # 순서대로 값에 넣음.

retData = deQueue()
print('손님 이리로: ',retData)

print('다음 손님 준비 하세요-->',peek())

retData = deQueue()
print('손님 이리로: ', retData)

print('출구 <--',queue,'<-- 입구')

enQueue('수셈') # 문제가 있다..보충 필요!

"""결과 : 
출구 <-- ['아이네', '징버거', '릴파', '주르르', '비챤'] <-- 입구
손님 이리로:  아이네
다음 손님 준비 하세요--> 징버거
손님 이리로:  징버거
출구 <-- [None, None, '릴파', '주르르', '비챤'] <-- 입구
큐가 꽉찼다.
"""

## 순차 Queue_최종
## 보완
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :   # Case 1
        return False
    elif (rear == SIZE -1 and front == -1) : # Case 2 : Full.
        return True
    elif (rear == SIZE -1 and front != -1) : # Case 3 : 앞 여유
        for i in range(front+1,SIZE,1) :
            queue[i-1] = queue[i] # 앞으로
            queue[i] = None
        front -= 1 # 한 칸씩 땡김
        rear -= 1
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 가득 찼다.")
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐가 텅 비었다.")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 텅 비었다.")
        return
    return queue[front+1]

## 변수
SIZE = 5
queue =[None for _ in range(SIZE)]
front = rear = -1 # 초기화

## 메인

enQueue('아이네')
enQueue('징버거')
enQueue('릴파')
enQueue('주르르')
enQueue('비챤')
print('출구 <--', queue, '<-- 입구')   # 순서대로 값에 넣음.

retData = deQueue()
print('손님 이리로: ',retData)

print('다음 손님 준비 하세요-->',peek())

retData = deQueue()
print('손님 이리로: ', retData)

print('출구 <--',queue,'<-- 입구')

enQueue('수셈') 
print('출구 <--',queue,'<-- 입구')
enQueue('왁굳') 
print('출구 <--',queue,'<-- 입구')
enQueue('루석') 
print('출구 <--',queue,'<-- 입구')

""" 결과 :
출구 <-- ['아이네', '징버거', '릴파', '주르르', '비챤'] <-- 입구
손님 이리로:  아이네
다음 손님 준비 하세요--> 징버거
손님 이리로:  징버거
출구 <-- [None, None, '릴파', '주르르', '비챤'] <-- 입구
출구 <-- [None, '릴파', '주르르', '비챤', '수셈'] <-- 입구
출구 <-- ['릴파', '주르르', '비챤', '수셈', '왁굳'] <-- 입구
큐가 가득 찼다.
출구 <-- ['릴파', '주르르', '비챤', '수셈', '왁굳'] <-- 입구
"""

## 원형 Queue
# 원형큐 단점 : 한 칸을 사용 못함 즉,한 칸이 비워져 있음. front == rear이면 꽉찼지만 빈 것으로 처리.
def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1)%SIZE == front):        #(rear+1)%size 값은 나머지.. 즉 다시 0 으로 돌아온다.
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 가득 찼다.")
        return
    rear = (rear+1)%SIZE                #(rear+1)%size 값은 나머지.. 즉 다시 0 으로 돌아온다.
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):                 # 머리 꼬리가 같은지 확인
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐가 텅 비었다.")
        return
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 텅 비었다.")
        return
    return queue[(front+1)%SIZE]

## 변수
SIZE = 5
queue =[None for _ in range(SIZE)]
front = rear = 0 # 초기화
# 초기화

## 메인

enQueue('아이네')
enQueue('징버거')
enQueue('릴파')
enQueue('주르르')

print('출구 <--', queue, '<-- 입구')   # 순서대로 값에 넣음.

enQueue('수셈') 
print('출구 <--',queue,'<-- 입구')

retData = deQueue()
print('손님 이리로: ',retData)

print('다음 손님 준비 하세요-->',peek())

retData = deQueue()
print('손님 이리로: ', retData)

print('출구 <--',queue,'<-- 입구')

enQueue('수셈') 
print('출구 <--',queue,'<-- 입구')
enQueue('왁굳') 
print('출구 <--',queue,'<-- 입구')
enQueue('루석') 
print('출구 <--',queue,'<-- 입구')













