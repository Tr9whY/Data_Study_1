"""
# 리스트
  - 리스트 정의,추가,삭제
"""

# 리스트는 여러 개의 데이터를 하나의 변수로 묶어 정의하는 컬렉션 데이터 타입.
# 빈 리스트 정의
list_a = []
print(list_a,type(list_a))

list_b = [1,2,3,4]
print(list_b, type(list_b))

# 혼합 데이터 타입
list_c = ['21','푸바오', 3, 3.14, '강아지']
print(list_c,type(list_c))

# 리스트 추가 .append
# >> 리스트의 맨 뒤에 값 추가

list_c.append(10)
print(list_c)

# 삽입 insert()
# 리스트는 순서가 있음(indexing)
# list의 특정 위치에 값을 추가.

print(list_b)
list_b.insert(2,10)
print(list_b)

print(list_c)
list_c.insert(2,3)
print(list_c)

# list의 값 제거 (remove, del)
# remove 특정 값을 제거

print(list_c)
list_c.remove(3)
print(list_c)

list_c.remove(10)
print(list_c)

# del
# del(=delete) 데이터를 직접 지명해 주는 게 아니라, 위치로 삭제할 데이터를 알려줌.

print(list_b)
del list_b[2]   #위치 지정.
print(list_b)

"""# 리스트의 접근
  - 인덱싱 : 위치(숫자)로 리스트의 값을 가져옴
  - 슬라이싱 : 전체 리스트를 일부 잘라서 가져옴
   
"""

list_f = [1,3,5,7,9]

# indexing
# 파이썬 인덱스 시작 0부터 시작
print(list_f[3])

# 슬라이싱(slicing)
print(list_f[1:3])
print(list_f[2:])
print(list_f[:3])
print(list_f[:-1])    ##  빈번하게 사용
print(list_f[::2])
print(list_f[::-1])

"""# 리스트의 함수"""

n_list = [2,4,6,8,10]

# len() : length 줄임. 리스트의 크기(길이) 알려줌
print(len(n_list))

# index : 요소가 들어가 있는 데이터 위치 반환
print(type(n_list))
print(n_list.index(2))
print(n_list.index(8))

team_korea = ["황선홍","이강인","손흥민","조현우"]

print(team_korea.index("손흥민"))
print(team_korea.index("이강인"))

# print(team_korea.index("카리나"))
# ValueError: '카리나' is not in list

# pop : 팝팝! 튀는 것처럼 마지막 제거
# 뒤에서부터 리스트 값을 하나씩 뺌
print(team_korea)
print(team_korea.pop())

print(team_korea)

골키퍼 = team_korea.pop()

print(골키퍼)

team_korea = team_korea.copy()

print(team_korea)

# sort : 정렬 (default(기본값) : 오름차순)
print(n_list)

print(team_korea)
team_korea.sort() #a,b,c 가나다 순

print(team_korea)

n_list.reverse()
print(n_list)

n_list.sort()
print(n_list)

# sort(), sorted() 함수 비교
# sort() : 정렬된 리스트 보여줌
# sorted() : 원래 리스트를 수정하지 않음 >> 정렬된 리스트를 보여주기만 함.
print(team_korea)
sorted_data = sorted(team_korea)
print(sorted_data)

"""# Dictionary(딕셔너리)
    - 딕셔너리의 정의, 추가, 삭제 접근
"""

dict_a = {}
dict_b = {"A":1,"B":"Baby", 3:3, 4:"Four"}
dict_c = {"flower" : ["진달래","개나리","목련"]}

dictA = {}
dictB = {"A":1,"B":"Baby",2:3,4:"Four"}
dictC = {"flower" : ["진달래꽃","벚꽃","개나리"],3:31}

"""# < Dictionary의 함수 >
- keys()    - 딕셔너리의 키를 리스트로 가져온다.
- values()  - 딕셔너리의 값을 리스트로 가져온다.
- items()   - 딕셔너리의 키 - 값 쌍을 튜플로 묶어 가져온다.
- get()     - 딕셔너리의 '키'에 맞는 값을 가져온다.
- in()      - 딕셔너리 안에 '키'가 있는지를 확인한다.
- clear()   - 딕셔너리의 모든 요소를 삭제한다.
"""

#추가
# >> key-value 쌍을 명시해 주어야 함.
# 딕셔너리는 순서가 없음

dict_a['감탄사'] = 'wow'

print(dict_a,type(dict_a))

# 접근 : 반드시 키로 접근한다.
print(dict_a['감탄사'],type(dict_a)) #[키!]

#삭제 : key를 전달해 준다.
del dict_a['감탄사']
print(dict_a)

# Dictionary 함수
# keys
print(dict_b)
# keys : 딕셔너리의 키들(keys)만 보여줌.
print(dict_b.keys(), type(dict_b.keys()))

# values : 딕셔너리의 값(value)만 보여줌.
print(dict_b.values())

# items (제일 많이 씀)
# tuple 형태로 key-value 쌍으로 짝지어 전달함.

print(dict_b.items(),type(dict_b.items()))

# get : key 를 전달하여 값을 가져옴

print(dict_b.get(3))

print(dict_b.get('B'))

print(dict_b.get(7))
# 값이 없으니까 반응이 없음

# in 은 "key" 유무를 확인한다.
print(5 in dict_b)
print('B' in dict_b)

# clear()는 딕셔너리 모든 요소를 삭제한다.
dict_b.clear()
print(dict_b)
