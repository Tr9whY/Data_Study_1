# <Tupel(튜플)>

t1 = ()
t2 = (1,2,3,4,5)
t3 = (2,4,'판다','강아지') # 컬렉션 타입(여러 개의 자료형 소유 가능)

print(t2[0])
print(t2[-1])

# 인덱싱(Indexing)_을 통해 튜플 내부 접근 가능
# 파이썬 index는 0 부터 시작
# 파이썬에서 index에 '-' 기호가 붙으면, 뒤에서부터 숫자를 센다. (-1,-2,-3....)
print()
print(t3[-2])

# 슬라이싱 (Slicing)
# >> 튜플 안의 값의 일부만 가져오는 것

print(t2[2:])
print(t2[:4])
print(t2[::2])
print(t2[::-1]) # reverse

"""튜플의 더하기, 곱하기"""

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2

print(t3)

t4 = (1,2,3,4)
# t4[-2] = 5
# tuple은 값을 임의 변경 불가(immutable)
t4 = list(t4)
t4[-2] = 5
t4 = tuple(t4)
print(t4,type(t4))

t5 = t1 * 5
print(t5)

"""Set(집합)"""

t4

t4 = list(t4) # tuple >> list 자료형 변경

# extend() : list의 현재 list 끝에 추가
t4.extend([4])

t4 = tuple(t4)

print(t4, type(t4))

s1 = ()
s2 = set(t4)          # tuple >> set 변경
print(s2, type(s2))   # set : 중복제거, 순서가 없음

#s2[3]      , 순서가 없음
#TypeError: 'set' object is not subscriptable
# 순서가 없으니까 indexing이 안됨
# 접근할려고 하면 tuple, list로 변환해야함.

tto1 = tuple(s2)
print(tto1,type(tto1))
print(tto1[-1], type(tto1))

tto2 = list(s2)
print(tto2,type(tto2))
print(tto2[-2])

"""#값 추가"""

s2

# 한 개의 값 추가   .add()
s2.add(6)
print(s2,type(s2))

# 여러 개의 값 추가    .update([])
s2.update([3,6,7,8])
print(s2)

# 특정 값 제거    .remove()
print(s2)
s2.remove(7)
print(s2,type(s2))

"""# 교집합, 차집합, 합집합

"""

t2 = set([1,2,3,4,5])
t3 = set([2,4,'판다','강아지'])

# 교집합
print(t2.intersection(t3))
print(t2 & t3)

# 차집합
print(t2.difference(t3))
print(t2 - t3)

# 합집합
print(t2.union(t3))
print(t2 | t3)

"""# 리스트"""

listA = []
listB = [1,2,3,4,5]
listC = [3,'강아지',2,4,'고양이']

#리스트 추가
#listA.append()      # 바로 뒤에 데이터를 추가한다.
#listB.insert()      # '자리' 에 데이터를 추가한다.

#리스트 삭제
# listA.remove()    ( 삭제하려는 데이터 ) # 리스트에서 첫번째로 나타난 ‘삭제하려는 데이터’를 삭제한다
#del listA[n]       # 리스트의 n번째 요소를 삭제한다.

listA.append(24)
print(listA) # 24가 추가 되었음

listB.insert(4,3)
print(listB) # 3번째 자리에 4라는 데이터 추가

listB.remove(3)
print(listB) # 앞쪽의 첫번째로 나온 3 데이터를 삭제

del listC[2]
print(listC) # 0,1,2 순서대로 데이터 2가 삭제됨
