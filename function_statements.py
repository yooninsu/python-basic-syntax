# a = 100
# # 특정한 input 값이 있을 때, 
# # 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
# # 그런데, 해당 연산은 매번 빈번하게 사용이 된다고 가정하자.
# #
# # 복잡 로직의 연산을 함수화 시켜서 재사용할수 있게 해보자.
# # input값이 있어도 되고, 없어도 된다.
# # return 값이 있어도 되고, 없어도 된다.
# def myFunc(myInput):
#     calc = (((myInput + 10) * 20) / 10 ) ** 2
#     return calc
# result2 = myFunc(200)

# # 함수명 myPlusFunc
# # 함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하라.
# def myPlusFunc(input):
#     total = 0
#     for a in range(1,input+1):
#         total += a
#     return total
# result = myPlusFunc(10)

# # input값을 2개를 받아 2값을 더한뒤, *2만큼 하여 reutrn하는 함수를 만들어보자
# # 그리고, 해당 함수를 호출하여 호출된 결과갑승ㄹ result에 담아 출력해보자.
# def myFunc2(input1,input2):
#     total = 2 * (input1 + input2)
#     return total
# a = myFunc2(10,20)
# print(a)
 
# # list의 index 함수를 쓰지 않고,
# # for문 또는 whilie문을 통해 몇 번쨰 인덱스에 있는 값인지
# # print 해보자
# lista = [1,4,6,9]

# def myIndex(num,llist):
#     result = -1 # 값이 없으면 -1이 나오
#     for a in range(len(llist)):
#         if num == llist[a]:
#             result = a
            # break를 할 필요 없이, 바로 return을 해도 된다.
            # return하게 되면 함수전체가 강제 종료된다.
#             break # 넣지 않으면 인덱스 함수와 달리 중복되는 경우 계속해서 뒤에 같은 숫자를 찾아낸다.
#     return result
# # 위의 for문을 활용하여 myIndex라는 이름의 함수를 만들고자 한다.
# # input값이 2개(list,찾고자 하는 값), print는 함수 내에서 하지않고, return에 값을 담는다.
# print(myIndex(9,[1,2,3,4,5,6,7,8,9,0,12,3,14]))

# 원의 넓이를 구하는 함수를 만들어 출력하라.

# def CircleSize(num):
#     size = num ** 2* 3.14
#     return size
# num = int(input("반지름의 길이를 입력하시오."))
# size = CircleSize(num)
# print("원의 넓이:" + str(size))

# def hello1():
#     print("hello1 python!")

# def hello2():
#     return("hello2 python!")

# hello1()
# print(hello2())

# # 입력값의 개수가 정해져 있지 않고 multiple한 함수 * 
# def sum(*nums):
#     total = 0
#     for a in range(len(nums)):
#         total += nums[a]
#     return total

# totalValue = sum(1,2,3,4,5)
# print(totalValue)

# # 2개 이상의 리턴 값이 있는 경우 # 튜플 형태로 데이터 return
# def cal(a,b):
#     result1 = a + b
#     result2 = a - b
#     result3 = a * b
#     return result1, result2, result3


# calValue = cal(1,2)
# print(calValue)

# # 계산한 첫번째 결과값은 xx, 두번째 결과값은 yy, 세번째 결과값은 zz
# print(f"계산한 첫번째 결과값 {calValue[0]}, 두번째 결과값 {calValue[1]}, 세번째 결과값 {calValue[2]}")

# # 함수에서 default값 미리 세팅
# def cal(a,b,c):
#     if c == 'plus':
#         result = a + b
#     elif c == "minus":
#         result = a - b
#     elif c == 'multiply':
#         result = a * b
#     return result
# # 더하기한 값 출력
# # 마이너스한 값 출력
# # 곱하기한 값 출력
# # c = input("type plus, minus, or multiply:")
# # print(cal(1,2,c))

# # 매개변수의 순서를 안 맞추고도 원하는 매개변수의 자리에 값을 넣어 함수를 호출하는 방법
# def whoAreYou(name, age, gender):
#     print(f'제 이름은 {name}이고, 나이는 {age}, 성별은 {gender}입니다. ')

# whoAreYou(19, '홍길동', '남자') # 옵션이 없으면 순서대로만 들어가짐
# whoAreYou(age = 19, name = '홍길동', gender = '남자') # 매개변수를 입력하여 사용

# # 파이썬에서 default값 세팅하는 대표적인 예시가 print함수
# # print 2개를 사용해서 줄바꿈 없이 hello world라고 출력이 되도록 만들어보자
# print('hello', end = " ")
# print('world')

# # 지역변수와 전역변수
# # 지역변수 : 함수내에서의 변수, 함수내에서만 유효
# # 전역변수 : 함수밖에서의 변수, 함수내에서도 인식은 할 수 있음 
# a = 100
# def sum(a, b):
#     # 여기서 a의 값은 100인가? 10인가?
#     # 전역변수인 a = 100보다, 함수내에서 선언한 a = 10 우선적으로 인식
#     result = a + b
#     return result
# result = sum(10,20)
# print(result) # 함수 내의 result라는 변수는 함수 밖에서는 인식 불가
# # 우리가 result를 프린트 할 수 있었던 것은, 함수 내에서 어떤 값을 return 해줬기 때문.
# print(a)

# lista = [10, 20, 30, 40]
# # for문마다 같은 변수를 사용하는 것은 전역변수이기는 하지만, 재할당을해서 사용하는 것이므로 어차피 reset되서 문제되지 않는다.
# for a in range(len(lista)):
#     print(a)
# for a in range(len(lista)):
#     print(a)
# print(a)    

# # 이중 for문을 사용할 떄는 문제가 될 여지가 있다.
# # 다중 for문을 쓸 때는 상위의 for문의 변수를 잃어버리게 되므로, 다른 변수명 사용
# for a in range(len(lista)):
#     for a in range(len(lista)):
#         print(a)


# # 함수 내에서 전역변수에 영향을 끼치는 방법 : global
# # 기본적으로 함수 내에서 함수 밖의 전역변수를 수정할 수 없다.
# # 그 이유는 저장되는 메모리 위치가 다르기 떄문에
# result = 0
# def sum(a):
#     global result
#     result += a 
#     return result

# value = sum(10)
# print(value)

# 데이터 영역에 전역변수 저장(프로그램이 로드될 때 값이 정해진다.), 힙 영역에 객체 저장, 스택 영역에 지역 변수 저장
# 스택 영역에서 데이터 영역의 전역 함수를 인식은 할 수 있지만 수정은 불가능(저장된 메모리가 다르기 때문에 # global을 사용하면 가능).

# # 객체는 힙메모리 영역에 저장되는데, 함수내에서도 접근하여 추가/수정이 가능하다.
# # 스택영역에 있는 지역변수는 함수가 끝나면 휘발되지만, 힙메모리는 휘발되지 않는다.
# lista = [2,3,4]
# def appendTest(input1, input2):
#     input1.append(input2)

# appendTest(lista,5)
# print(lista)                                                                   

# # 만약에 지역변수가 함수호출이 끝난 뒤에도 남아있다면 어떻게 될까?
# def test1(result):
#     result = 10
#     return result
# def test2(result):
#     result += 100
#     return result
# a = test1(20)
# b = test2(20)


# #아래의 선택정렬을 함수화 시켜서 활용해보기
# lista = [93,45,21,30,20,94,66,71,45]

# def mySort(lista):
#     for a in range(len(lista)-1): 
#         for b in range(a+1,len(lista)): 
#             if lista[a] > lista[b]:
#                 temp = lista[a]
#                 lista[a] = lista[b]
#                 lista[b] = temp
#     return lista # return이 필요없는 이유, lst의 메모리에 접근해서 값을 바꾸기 때문에 상관없음

# lst = [5,1,2,3,1,4,6,8,23,4,19]
# lst.sort()
# list.sort(lst)
# mySort(lst)
# print(lst)

# lista에 listb를 담으면, 객체의 주소가 복사가 되게 된다.
# 그래서 listb가 lista와 동일한 주소, 동일한 데이터를 갖게 된다.
lista = [5,1,2,[1,2,3]]
listb = lista
# 주소 출력하는 함수 :id
print(id(lista))
print(id(listb))
# lista와 값은 갖되, 동일한 메모리 주소가 아니게 할당하고 싶으면 copy함수 사용
import copy
# 얕은 복사 즉,. 객체 안의 객체의 값은 (메모리) 주소로 복사가 된다.
# 깊은 복사는 copy.deepcopy를 사용하여 객체의 객체도 모두 value로 복사
listb = copy.copy(lista) # [5,1,2,객체의 주소]
print(id(listb))
print(listb)
lista[0] = listb[1]
lista[1] = listb[0]
print(lista)
