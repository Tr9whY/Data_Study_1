
"""method

"""

list_ = []
list_.append(1)
list_.append(2)
list_.append(3)
print(list_)

list_2 = ['banana','apple','caramel']

list_2.sort()
print(list_2,type(list_2))

list_3 = [5,4,3,2,1]
list_3.sort()

print(list_3,type(list_3))

"""# < Sequence의 indexing과 slicing >
- indexing : sequence에서 한 원소를 가져오는 것.
- slicing : sequence 에서 일부분을 가져오는 것
"""

list_4 = [1,2,3,4,5,6]
print(list_4[3:])
print(list_4[:2])
print(list_4[:])
print(list_4[::-1])
print(list_4[:-1])
print(list_4[-1:])

my_str = 'impossible'
my_list = ['Apple','Banana','Watermelon','Durian']

print(my_str[2])
print(my_list[2:])

"""# sequence 길이와 멤버 조사하기"""

my_str = 'abc'
print(len(my_str))
print('d' in my_str)
print('b' in my_str)

my_dict = {"사과":"apple","바나나":"banana","당근":"carrot"}
print(my_dict['당근'])
del my_dict['당근']
print(my_dict)
my_dict['망고']='mango'
print(my_dict)

bad_dict = {1:"one",1:"yi"}
print(bad_dict,type(bad_dict)) #키는 하나에 하나값만 존재한다. 안그러면 덮어 씌움

good_dict = {1:['one','yi'],2:['two','er']}
print(good_dict)
print(good_dict[2])

print(good_dict[2][1])
print(good_dict[1][0])
print(good_dict[1])

#{[1,2,3]:"num"}
#TypeError: unhashable type : 'list'
# 리스트는 key 로 사용하지 못함.

{(1,2,3):"num"}   # tuple(상수) : immutable (변경 불가) >> 고정된 값 >> dict 가능

my_dict = {}
my_dict[1] = 'integer'
my_dict['a'] = 'string'
my_dict[(1,2,3)] = 'tuple'

print(my_dict)

# try ~ except : 에러 방지용

my_dict = {}

my_dict[1] = 'integer'
my_dict['a'] = 'string'
my_dict[(1,2,3)] = 'tuple'

try:
  my_dict[[1,2,3]] = 'list'
except TypeError:
  print("unhashable type : 'list' >> list는 딕셔너리의 key가 될 수 없다.")
