"""
*_print()실습
"""

print("Hello Python.")

"""#기본자료형"""

# 숫자 50과 숫자 50을 더해서 출력하기

print(50+50)

# 문자열(String)
# 문자와 문자 더하면 >> 옆에 붙는다.
print("50"+"50")

# 파이썬에서 여러 개의 원소(element, 숫자, 문자)를 담는 그릇 >> 리스트(list 목록)
print([50]+[50])

"""# 변수
- 변하는 수
"""

#파이썬 변수의 정의

apple = 1
print(apple,type(apple))

Apple = '사과'
print(Apple,type(Apple))

print(True, type(True))
print(False, type(False))

#정수와 소수(부동소수점/실수)

A = 1.2
print(A,type(A))
B = 2
print(B, type(B))
print(A+B, type(A+B))

print(5//3)
print(5%3)

"""# 문자열"""

가 = 'hello'
print(가)

나 = " good morning" #space(빈 공백)도 문자로 인식.

print(나)
print(가+나)

A = "Hello"
B = ', Good Mornig'
print(A+B)

"""# Boolean"""

A = True
B = False

print(A)
print(B)

# != : 다르다
print(A==B)
print(A!=B)
print(A or B)
print(A and B)
print(not False)
print(not True)

"""# 변수에는 정수, 실수 같은 숫자를 저장할 수 있다.
- 영어나 한글과 같은 문자도 저장 가능.
- 이런 문자들의 집합도 리스트로 저장 가능.
- 리스트 : 여러 원소(Element)를 담는 그릇
"""

num1 = 1
num2 = 2
print(num1 - num2)

char = 'a'
print(char)

List_ = [1,'a','python']
print(List_)

# 그 목록(List_)에 원소 몇 개 있니?
len(List_)

A =1
A += 1
print(A)

B = 1
B -= 1
print(B)

A = 1
B = 32
print(A > B)

C = -3
D = -0.2
print(C <= D)

A = 1
B = 32
print(A == B)

C = -3
D = -0.2
print(C != D)

A = True
B = False
print(A and B)
print(A or B)
print(not A)
print(not B)

A = '사과'
B = ['사과','배','참외','수박','복숭아']
print(A in B)

C = 'apple'
D = ['Apple', 'pear', 'watermelon', 'peach']

print(C in D)

A = '사과'
B = '사과'
print(A is B)
C = 12
D = 12
print(C is not D)

"""# Summary

- 변수를 정의할 때는 = 를 사용한다.

- 변수 명에는 영어 소문자, 영어 대문자, 숫자, 언더스코어(_)를 사용할 수 있다. (단, 숫자는 맨 처음에 올 수 없다)

- 몇 가지 특수한 영어 단어(예약어)는 변수명으로 사용할 수 없다.

- 변수에는 int, float, bool, string & tuple, set, list, dictionary 의 자료형이 들어갈 수 있다.

- int, float, bool, string 은 수치 자료형으로, 단일 데이터를 저장한다.

- tuple, set, list, dictionary는 컬렉션 자료형으로, 여러 데이터를 저장한다.

- 변수는 연산이 가능하다.

- 파이썬 연산자는 할당연산자(+=), 산술연산자(>=), 논리연산자(and), 멤버연산자(in), 식별연산자(is)가 있다.
"""

a =+ 1
b =- a
b

a = '사과'
b = '사과'

print(a is b)

# is 와 == 의 차이

#1. is 와 == 동등성 비교
#2. == 연산자 : 두 객체(a, b...) 값이 동일한지 비교
#3. is 는 식별자가 동일한지 비교.

a = [1,2,3]
b = [1,2,3]
c = a

print(a == b) #값 비교

print(b is a) # 값은 같다, 그러나 서로 다른 메모리 위치에 있음.
print(c is a)

e = 1,2,3
print(e)
print(type(e)) #tuple 상수 (변하지 않는 수)

f = [1,2,3]
print(f)
print(type(f)) #List 변할 수 있는 수

c = 12
d = 12
print(c is not d)
# c와 d가 실제로 메모리의 동일한 객체(정수객체)를 참조하니까.
# 동일한 객체

print(len(List_),type(List_))

my_var_1 = 'a'
my_var_2 = List_


print(List_)
print(List_[0])
print(List_[1])
print(List_[2])



print(my_var_1 + my_var_2[2]) # 같은 데이터 타입(자료형)이여야 연산이 가능함.

a = "345" #문자 >> 정수
a = int(a)
print(a,type(a))
b = '3.14'
b = float(b)
print(b,type(b))
