"""
# 원소로 반복하기 for()
"""

my_sum = 0 # 초기화

nums = [1,2,3]

for i in nums:
  my_sum += i

print(my_sum)

nums = [1,2,3,4,5,6,7,8,9,10]

for i in nums:
  print(i)

mix = '쌀'
mix = '쌀'*100

count = 0

for i in mix:
  if i == '쌀':
    count += 1 # count = count + 1

print(count)

mix = ['쌀','보리','쌀']
mix[1]

mix_100 = '쌀' * 100
count = 0

for i in mix_100:
  if i == '쌀':
    count += 1 # count = count + 1

print(count)

"""반복할 숫자의 범위"""

#range(start, end) >> [start,start+1,....,end-1]
range(10)

list(range(10))   # 0부터 시작해서 10개

for i in range(10):
  print(i)

for i in range(1,11):   # 범위 지정이 가능하다
  print(i)

for i in range(5):
  print("안녕"*2)

print("뭐해")

for i in range(10):
  print("코딩")

"""# 구구단 출력
for - range() 활용

"""

for i in range(1,10):
  print("9 *",i , "=", 9*i)

for i in range(2,10):
  print ("-"*5,i,"단","-"*5)
  for j in range(1,10):
    print(i,'*',j,'=',i*j)
    if j == 9:
      print()

