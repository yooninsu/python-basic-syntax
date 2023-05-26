# set은 (수학) 집합이라고 부르기도 한다.
# set의 특성은 딕셔너리와 마찬가지로, index가 없고, 중복이 없다.
s1 = {'이름', '나이', '성별'}
# list의 중복을 제거하기 위해서 list를 가지고 set으로 형 변환 시키는 방식도 많이 사용
s1 = set(['이름', '나이', '성별']) # 형 변환
print(s1)
s2 = set('test') # = set(list('test'))
print(s2) # {'s', 'e', 't'}
# 순서가 없으므로 index로 접근이 불가
# print(s1[0]) # set object is not subscriptable



lista = ['A', 'A', "A", "B", 'B', 'AB', 'O']
# 이 반 학생들의 혈액형 종류는 총 몇개인가?
print(len(set(lista))) # 4 
# A, B, AB -> 3개
setA = set(lista)
# setA의 값을 하나씩 출력하려면? setA[0], setA[1] 불가
for a in setA:
    print(a)

# 합집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
# 프로그래밍에서 | 기호는 or(또는)을 의미
s3 = s1 | s2
s3 = s1.union(s2)
# 교집합
# 프로그래망이서 &은 일반적으로 and(그리고)를 의미
# ampersand라고 부른다.
s4 = s1 & s2
s4 = s1.intersection(s2)
# 차집합 
s5 = s2- s1
s5 = s2.difference(s1)
print(s3)
print(s4)
print(s5)

#집합에서 값 추가: add
s1 - {1,2,3,4,5}
# 7을 추가한다음에 s1출력
s1.add(7)
print(s1)

#갑 여러개 추가 시 update 함수(딕셔너리와 동일)
# s1에 s2를 update
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8}
s1.update(s2)
print(s1)

# set 값 삭제 시 remove, discard 함수 사용
s1 = {1,2,3,4,5,6}
# discard : remove와의 차이점은 삭제할 값이 존재하지 않아도 에러가 발생하지 않는다는 점

s1.remove(6)
s1.discard(5)
print(s1)

# boolean(불형) 타입
# in, not in : in(또는 not in) 뒤에 iterable한 자료형이 나온다.
# a in lista, a not in lista, a in dicta.keys(), a in seta

# 비어있는 값들은 거짓, 값이 들어있으면 참

listA = [1,2,3]
while listA:
    print('참입니다.')
    listA.pop()

    