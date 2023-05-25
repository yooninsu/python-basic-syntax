#tuple
# tuple은 변경불가능한 자료형으로서, ()를 통해 표현
t1 = (1,2,'a','b')
print(t1)
print(t1[0])
# indexing, slicing 둘 다 list와 동일하게 허용

# #삭제, 변경 불가
# del t1[0]
# print(t1)

# 소괄호()로 묶어 값을 입력하며, 내부 값은 콤마로 구분
# 숫자, 리스트, 문자 허용
# 튜플 사용이유: 불변 값 사용시 메모리 효율적 -> 개발자가 해당 자료를 수정하지 못하도록 강제적으로 지정한 것.
# in : if a variable is invovled in any iterable data such as list and tuple, it would be true unless it is false.
# 리스트에 비해 메모리 효율적
# 더하기, 곱하기 가능

# dictionary
#리스트에 비해 메모리 효율적
# the format of dictionary is combined with key and value.
# 영어사전에서 단어와 뜻으로 이루어져 있는 것에서 유래.
# 순서가 없다.
# key를 이용해 값의 추가, 삭제, 수정 등 가능.
# key는 중복이 불가, value는 다른 key에도 중복이 가능(존재할 수 있다.)
# hash(ruby), json, map or hashmap(java) 등등

dic1 = {'이름': '홍길동', '나이': 25, '성별': '남', '성별': '여'} 
print(dic1) #  {'이름': '홍길동', '나이': 25, '성별': '여'} it is automatically overwrited.
result = {'1': 80, '2': 90, '3':100, '4':10}
print(result)

#딕셔너리의 기본호출 방식은 변수명[key], 변수명.get(key)
print(dic1['나이']) # 25
print(dic1.get('나이')) # 25

# 리스트는 a = [value, ...] 딕셔너리는 a = {key:value, ...} 튜플은 a = (value, ...)
# 딕셔너리와 튜플은 a[index], 딕셔너리는 a[key]

# 딕셔너리 특징 2
# key와 value로 이루어져 있다보니, 순서가 의미가 없다. index로 접근 불가
# key를 가지고 value를 검색할 떄 해시함수를 통해 index를 찾다보니, 매우 빠른 속도를 보장.
dica = {10 : '열', 20: '스물', 30: '서른'}
# 해시 함수를 통해 메모리 주소를 할당

#list,dicitonary,set은 중복이 없다.
#딕셔너리의 동작원리 딕셔너리의 메모리 저장 방식 해시 함수란?

dic1['신분'] = '학생' # key:value 추가
print(dic1)

# del dic1['성별'] # 딕셔너리에서 키를 이용한 key:value 삭제
# print(dic1)

#딕셔너리에서 key목록만을 뽑아낼 떄
# iterable한 형태로 data가 뽑아져 나오므로 for문 사용 가능
keyList = dic1.keys()
print(keyList)

# # key, value 같이 출력할 때
# for a in dic1.items():
#   print(a)

# # 위의 keyList에서 각각의 값을 출력해보자.
# for b in keyList:
#   print(b)

# key를 출력해주는 for 문 안에서 value도 같이 출력하도록 해보자.
# for k in keyList:
#     print(k)
#     print(dic1[k])
  
# 위의 for문을 활용해서, key가 담긴 list를 만들고, value가 담긴 list를 만들어 각각 출력해보자.
listk = []
listv = []

for k in keyList:
  listk.append(k)
  listv.append(dic1[k])
print(listk)
print(listv)

# # 질문
# for k in keyList:
#   listk = listk.append(k)  # append 함수는 listk에 k값을 더하는 작업을 하는 none type을 producing하는 함수이다. 따라서 아무런 값을 갖고 있지않으므로 listk를 선언 불가
#   listv.append(dic1[k])


#value 목록을 뽑아낼때는 .values()
for v in dic1.values():
  print(v)

valueList = dic1.values()
print(valueList)

ll= list(valueList) # 타입 변환 가능
print(ll)

# dictionary의 확장: update 함수
dic1 = {"a":1, "b":2, "c":3}
dic2 = {"a":2, "d":4, "f":5}
dic1.update(dic2)
print(dic1)

