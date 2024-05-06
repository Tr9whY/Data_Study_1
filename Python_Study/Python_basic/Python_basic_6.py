""" 조건문과 반복문 """


"""# 주민등록번호로 성별 구별하기(남/여)"""
number = int(input())

if number % 2 == 0 :
  print("여자입니다.")
else:
  print('남자입니다.')
# 보충 필요

# 보충_주민등록번호로 성별 구별하기(남/여)
nums = str(input("뒷자리를 입력하세요."))
if int(nums[0]) % 2 == 0:
  print(nums,"여자입니다.")
else:
  print(nums,"남자입니다.")

# 의류 사이즈 분류
# 100에서 10단위로 커지는 사이즈에서
# 분류기준
# 1) size가 150이하: 아동용
# 2) size가 190이상 : 맞춤옷
# 3) 그 외: 성인용
size = int(input())

if size <= 150:
  print('아동용')
elif size >= 190:
   print('맞춤옷')
else:
  print('성인용')

# 조건에 100에서, 10단위라는 항목이 있어 이 조건문은 만족하지 않는다.

# 의류 사이즈 분류
# 100에서 10단위로 커지는 사이즈에서
# 분류기준
# 1) size가 150이하: 아동용
# 2) size가 190이상 : 맞춤옷
# 3) 그 외: 성인용
size = int(input())
if (size-100) % 10 == 0:
  if size <= 150:
    print('아동용')
  elif size >= 190:
    print('맞춤옷')
  else:
    print('성인용')
else:
  print("size는 100 이상, 10단위로 입력해주세요.")

for i in range(3):
  for j in range(2):
    print(i,j)

a = '*'
for i in range(11,0,-2):
  b = i*a
  print(b)

"""# < While >

- 무한 반복
- 반드시 정지조건 (pass, continue, break)
"""

# break : while 반복문 밖으로 빠져나감
# continue : 다음 소스 코드를 실행하지 않고 다음 단계로 넘어감
# pass : 아무 것도 하지 않고 넘김

number = 0      #초기화

while True :
  if number > 4:
    break

  print(number)
  number += 1

number = 0  # 초기화

while number < 6 :
  number += 1
  if number > 4 :
    continue
  print(number)

number = 0  # 초기화

while number < 6:
  if number % 2 == 0 :
    pass
  else:
    print(number,'홀수')
  number += 1

"""# < Comprehension >
- set,list, dictionary등 컬렉션 타입에 활용하는 문법이다.
- 반복문을 한 줄로 표현한다.
- 조건문을 한줄로 표현한다.
- 한 줄로 표현한 반복문과 조건문을 set,list,dictionary 형태로 만들어 준다.
- 주로 list 형식에 많이 쓰임
"""

number = [x for x in range(10+1)]
print(number,type(number))

odds = [x for x in number if x%2 == 1]
print(odds, type(odds))

odds = [x for x in number if x%2 ==1 if x < 5]
print(odds, type(odds))
