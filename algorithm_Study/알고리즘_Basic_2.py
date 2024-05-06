"""
<알고리즘_2>

1.선형 자료 구조
- 데이터를 한 줄로 순차적으로 표현한 형태.

2.비선형 자료 구조:
- 하나의 데이터 뒤에 여러 개가 이어지는 형태.

3. 알고리즘 :
- 어떤 문제를 해결해 가는 논리적인 과정
- 알고리즘 예:
        트럭에는 최대 7톤의 무게를 실을 수 있고 *단 1회만 운송 할 수 있다면,
        *선호도 합이 최대가 되는 동물을 태우는 방법은?

4.알고리즘 성능
- 빅-오 표기법(Big-Oh Notation)으로 O(f(n))형태
- 대표적인 함수는 O(1), O(log n), O(n) O(n log n), On2 ), (n3 ),O(2n.)

"""
# 전역 변수부
Fan = ['아이네','징버거','주르르','고세구','비챤']

# 데이터 추가(우왁굳에게 1회 후원)

# 1단계 : 빈칸 추가 -- append와 insert 차이 (리스트 끝 or 지정(index)) 
Fan.append(None)

# 2단계 : 마지막 칸에 새 친구 입력
Fan[5] = '우왁굳'
print(Fan)

## 데이터 삽입(릴파에게 40회 후원 == 릴파를 3등으로)
# 1단계 : 빈칸 추가
Fan.append(None)

# 2단계 : 한 칸씩 뒤로 이동(마지막 친구부터..3등까지)
Fan[6] = Fan[5]
Fan[5] = Fan[4]
Fan[4] = Fan[3]
Fan[3] = Fan[2]
Fan[2] = None

# 3단계 : 3등 후원 자리에 릴파 입력
Fan[2] = '릴파'
print(Fan)

# 데이터 삭제(고세구 후원 중단 == 5등 삭제)
# 1단계 : 데이터 지우기
Fan[4] = None
# 2단계 : 한 칸씩 앞으로 이동
Fan[4] = Fan[5]
Fan[5] = Fan[6]
Fan[6] = None
del Fan[6]
print(Fan)

print('-'*60)

# 전역변수
Fan = []

# 함수
def add_data(Wak):
    Fan.append(None)        # 1단계 : 빈칸 추가
    F_len= len(Fan)         # 선형 리스트의 길이를 파악!
    Fan[F_len-1] = Wak      # 2 단계 : 마지막 칸에 데이터 입력

def insert_data(position, Wak):
    Fan.append(None)        # 1단계 : 빈칸 추가
    F_len = len(Fan)        # 선형 리스트의 길이 파악

    for i in range(F_len-1,position,-1) : # 2단계 : 마지막 아이돌부터, 삽입할 위치까지 한 칸씩 뒤로 이동
        Fan[i] = Fan[i-1]
        Fan[i-1] = None
    # 3단계 : 위치에 아이돌 입력
    Fan[position] = Wak

def delete_data(position):
    # 1단계 : 데이터 삭제
    Fan[position] = None
    F_len = len(Fan)
    # 2단계 : 한칸씩 앞으로
    for i in range(position+1,F_len,1): #so Hard...
        Fan[i-1] = Fan[i]
        Fan[i] = None
    # 3단계 : 마지막 칸을 제거
    del(Fan[F_len-1])

# 메인 코드 부분
if __name__ == "__main__":
    select = 0              #초기화!!!!
    while (select != 4):
        select = int(input("번호를 선택(1: 추가, 2: 삽입,3: 삭제, 4: 종료)-->"))

        if (select == 1):
            data = input("추가할 데이터: ")
            add_data(data)
            print(Fan)
            
        elif (select == 2) :
            pos = int(input("삽입할 위치: "))
            data = input("추가할 데이터: ")
            insert_data(pos, data)
            print(Fan)
            
        elif (select == 3) :
            pos = int(input("삭제할 위치: "))
            delete_data(pos)
            print(Fan)
            
        elif (select == 4):
            print(Fan)
            exit
            
        else:
            print("1~4 중 하나를 입력하세요.")
            continue

