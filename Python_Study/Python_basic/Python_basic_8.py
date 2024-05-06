# List/Dict comprehension
# List comprehension : 리스트 안에 for문을 포함하여 한 줄로 작성할 수 있는 문법.
# ★[표현식 for 항목 in 반복가능 객체 if 조건문]

# 1부터 5까지 list로 만들어보자.
ls = []   # 초기화
for i in range(1,6):
    ls.append(i) #append는 마지막에 원하는 값을 넣어준다. 빈 칸에 들어가기 때문에 insert(위치, 입력 데이터)보단 append
print(ls)
print('='*30)

# List comprehension를 사용해보자.
ls = [i for i in range(1,6)] 
print(ls, type(ls))
print('='*30)

# 반복문을 사용, 0-10까지 숫자를 리스트로 만들어요.
number =  [i for i in range(0,11)]
print(number , type(number))
print('='*30)

# 1부터 5까지 숫자 중 2의 배수를 리스트로 만들어보자.
ls = []
for i in range(1,6):
    if i % 2 == 0:          # % : 나머지. //: 몫
        ls.append(i)
print(ls, type(ls))
print('='*30)

# List comprehension를 사용해보자.
ls = [i for i in range(1,6) if i%2==0]
print(ls)
print('='*30)

# 이중 for문 곱하기
ls = []
for i in range(1,6):
    for k in range(1,6):            # j를 쓰지 않은 것은 k가 눈에.. 더 잘보여서...
        ls.append(i*k)
print(ls, type(ls))
print('='*30)

#List comprehension를 이중 for문.
ls = [a*b for a in range(1,6) for b in range(1,6)]
print(ls)
print('='*30)
#  for문을 여러 개 사용하는 것도 가능하다.
"""
[표현식 for 항목1 in 반복가능객체1 if 조건문1
 for 항목2 in 반복가능객체2 if 조건문2..
 ...]
"""

# 구구단 만들어 보기
gugu = [i*k for i in range(2,10) for k in range(1,10)] # 2단 - 9단
print(gugu)
print('='*30)
# dict comprehension이란
# list comprehension과 마찬가지로 딕셔너리도 for문을 간편하게 이용할 수 있다.

names = ['gisan','wak','ine']
number = [1,2,3]
dic = {names[i]:number[i] for i in range(len(names))} # len(names) = 3
print(dic) 

print('='*30)
dic1 = {}
for i in range(len(names)): # 3이 아닌 len을 쓴 이유는 후에 무수한 데이터 때문에 버릇 길들이기..
    dic1[names[i]] = number[i]
print(dic1)

print('='*30)
names = ['gisan','wak','ine']
number = [1,2,3]
dic = {k:v for k,v in zip(names, number)}  
print(dic)
"""
# zip()함수는 여러개의 *반복가능한(iterable)객체를 인자로 받아 *튜플로 묶어주는 함수, *길이에 맞춰서 묶어줌.

ist1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)

for item in zipped:
    print(item)

결과 : 
(1, 'a')
(2, 'b')
(3, 'c')
"""
print('='*30)

dic1 = {}
names = ['gisan','wak','ine']
number = [1,2,3]
for i,k in list(zip(names,number)):
    dic1[i] = k 
print(dic1)
"""
dict22 = {}                 # 들어갈 자리 만들어줌.
dict22['욘두'] = '가오갤'    # dict[key] = value
print(dict22)
result ==> {'욘두': '가오갤'}
"""
print('='*30)
# dict comprehension 조건 달아보기
dic1 = {}
names = ['gisan','wak','ine']
number = [1,2,3]

dic1 = {i:k*5 for i,k in zip(names,number) if k % 2 != 0} # != : 같지 않다!
print(dic1)  # {'gisan': 5, 'ine': 15}

print('='*30)
# 1부터 100까지 5배수 합 list comprehenshion
ls = [i for i in range(1,101) if i % 5 == 0]
print(sum(ls))

print('='*30)
# 리스트를 딕셔너리에 넣고 키와 값을 바꾸어 출력하기.
dic1 = {}
names = ['gisan','wak','ine'] # 키
number = [1,2,3]              # 값

temp_1 = {v:k for k,v in zip(names,number)}
print(temp_1)

print('='*30)
# 이번엔 딕셔너리에서 키와 값을 바꾸어 출력하기.
temp_2 = {1: 'gisan', 2: 'wak', 3: 'ine'}
temp_3 = {v:k for k,v in temp_2.items()} # items : key-value를 각각 튜플로 묶은 객체를 반환하는 메서드.
print(temp_3)  # 결과 ==>> {'gisan': 1, 'wak': 2, 'ine': 3} 

# 리스트 안에 리스트를 하나의 리스트로 만들기..
temp_1 = [[100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

ls = []
for i in temp_1:
    for k in i:
        ls.append(k)
print(ls)

print('='*30)
# comprehension
temp2 = [k for i in temp_1 for k in i]
print(temp2)

# 딕셔너리 빈도값.
temp_5 = ['욘두','욘두','욘두','욘두','로켓','로켓','그루트','그루트','그루트','그루트','그루트']
# count를 이용해 볼것이다. print(temp_5.count('욘두')) --> 4

print('='*30)
test_1 = {}
for i in set(temp_5): # set : 함수는 중복된 요소 제거 고로 count에 중복 제거하고 값이 들어감.
    test_1[i] = temp_5.count(i) # count를 value로 갖는다면 for이 돌면서 i에 temp_5안의 값이 들어가고 찾는다..
print(test_1)

print('='*30)
test_2 = {i:temp_5.count(i) for i in set(temp_5)}
print(test_2)

print('test_3'*30)
test_3 = {i:temp_5.count(i) for i in set(temp_5)}
print(test_2)