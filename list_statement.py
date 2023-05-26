# list는 변수마다 값을 할당해서 사용하기에, 관리의 어려움이 있으므로
# 한 변수에 값을 집합시켜놓은 것.

a = "김돌쇠"
b = "김갑돌"
c = "김갑순"

#  하나의 변수로 여러개의 데이터를 관리
# list의 경우에 [] 대괄호를 사용하여 데이터를 지밯ㅂ
lista = ["a","b","c","d","e","f","g"]

# list안의 각각의 값에 접근할 때에는 index를 사용
# print(lista[0])
# print(lista[1])


# 여러 개의 데이터를 범위를 지정허ㅐ서 가져오고 싶을 때는 slicing 사용
# 슬라이싱의 결과값은 같은 list로 출력
# 0~5번 째까지 출력
print(lista[:5])

# 0~5번쨰까지 출력한 결과물의 type 출력
print(type(lista[:5]))

# 문자열은 메모리 내부적으로 list와 유사한 자료구조 
# 문자열은 값을 추가하거나 수정할 수 없다.
a = "hello"
a = "hello12"
# 재정의 과정
# 그러나 list는 값의 추가, 삭제, 수정이 가능한 구졸를 가지고 있다.

#연습문제(인덱싱)
list_ex1 = ['a','b','c',[1,2,3]]
# 변수 number에 [1,2,3]을 담아 출력하라.
number=list_ex1[3]
print(number)
# number에 담음 값 중 1과 3을 더해 4를 출력하라
print(number[0]+number[2])
# list안에 list의 값을 조회하는 방법
print(list_ex1[3][0]+list_ex1[3][2])

#정렬
lista = [10,1,2,6,3,4]

# 리스트 더하기
# list를 2개 선언하고 만들어서, 2개를 더해서 하나의 리스트로 만들어보자 그리고 출력
listb = [1,2,3,4]
listc = [2,3,4,5]
print(listb+listc)
print(listc*5)

# 리스트 길이 구하기 : len
print(len(lista))

# 리스트 값 수정하기
# -> 1개의 값만 바꿀 땐 1개의 값으로 대체
# -> 여러 값을 바꿀 땐 다른 리스트로 대체

lista = [1,3,4,5,7,9]
lista[1] = 4
print(lista)
lista[2] = [5,5,5]
print(lista)

# 리스트 요소 개수 세기
lista = ['1','2','3','4','1','1','3']
print(lista.count('1'))

#리스트 요소 삭제하기
lista = ['1','2','3','4','1','1','3']
# 3번째 값을 삭제하라
del lista[2]
print(lista)
lista = ['1','2','3','4','1','1','3']
# 2번째 ~ 5번째 값을 삭제하라
del lista[1:5]
print(lista)

#리스트 요소 삭제하기 (remove)
lista = ['1','2','3','4','1','1','3']
lista.remove('4')
print(lista)

# 모든 특정한 숫자 9값을 삭제하려면?
# using del, for range
# method 1
lista = [1,9,4,9,5,7,8,9]
count = 0
for i in range(0,len(lista)):
    if lista[i-count] == 9:
       del lista[i-count]
       count += 1
print(lista)

# method 2
listb =[]
for i in range(0,len(lista)):
    if lista[i] != 9:
        listb = listb+[lista[i]]
print(listb)

# method 3
for a in range(0, len(lista)):
    if 9 in lista:
        lista.remove(9)
    else:
        break
print(lista)

# 리스트 값 추가하기(append, insert,extend )

#list.append : 리스트 맨 뒤로 추가
lista = [1,3,5,7]
# 9,10을 append이용해서 추가해서 출력
lista.append(9)
lista.append(10)
print(lista)
# list insert : index를 지정하여 추가 가능
# lista.insert(2,"abc") 추가 후 출력
lista.insert(2,"abc")
print(lista)

# list extend : iterable객체를 list에 추가할 때 사용
# extend는 각 요소를 꺼내어 맨 뒤에 추가
listb = [10,20,30]
lista.append(listb)
print(lista)
lista.extend(listb)
print(lista)

# list의 정렬은 sort() 함수 사용
# sort() 오름차순 정렬 
# reverse=True 옵션을 주면 내림차순 정렬
numa = [5,3,18,4,2,1]
numa.sort()
print(numa)

chlist = ['brad', 'john', 'amy']
chlist.sort()
print(chlist)

# list 뒤집기 : reverse()
chlist.reverse()
print(chlist)

# list 위치반환(index)
lista = ['김돌쇠', '김갑돌', '김갑순', '김철수']
print(lista.index('김철수'))

stra = "courage is very important. Like a muscle, it is strengthened by use"
print(stra.index("b"))

# 마지막 요소 끄집어 내기 : pop()
# remove and return the last value
lista.pop()
lastvalue = lista.pop() #제거한 값을 확인가능
print(lista)
print(lastvalue)




# 문자 리스트를 문자열로 만들기
lista = ["hello", "world", "python"]
st1 = ""
st2 = st1.join(lista)
print(st2)

# 문자열을 문자 리스트로 만들기
sta = "hello world python"
mySta = list(sta) #형 변환
mySta2 = sta.split()
print(mySta)
print(mySta2)

#최대값 구하기
lista = [100, 20, 30,50,8,200]
for n in lista:
   for i in range(len(lista)):
      if n < lista[i]:
         n = lista[i]
      else:
         n
print(n)

# 최소값, 최대값
mx = lista[0]
mn =  lista[0]
for n in lista:
   if mx < n:
      mx = n
   if mn > n:
      mn = n
print(mx,mn)

# 방법3.sort
lista.sort()
maxA = lista[len(lista)-1]
minA = lista[0]
print(maxA,minA)

#내림차순 정렬
listb = [100,20,30,50,8,200]
array= []
for i in range(len(listc)):
   mini = i
   for j in range(0, len(listb)-i):
      if listb[i] >= listb[j]:
         i = j
   print(i)
   print(listb[i])
   array.append(listb[i])
   listb.remove(listb[i])
   print(array)
   print(listb)
   print(i)
  