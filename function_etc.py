
# 람다함수 : 1)함수를 간편하게 표현하기 위한 방식 2) 함수를 변수에 담기 위한 방식
# lambda 매개변수: 실행문
# def add(a,b):
#     return a+b
# print(add(1,2))

# add_lambda = lambda a, b : a+b
# print(add_lambda(1,2))
# # 매개변수 a를 입력했을 떄, a의 제곱이 출력되는 lambda함수 생성
# pow_lambda = lambda a: pow(a,2)
# print(pow_lambda(15))

# #list에 람다 함수를 담아서 사용 가능.
# cal_list = [lambda a,b: a+b,lambda a,b: a-b, lambda a,b: a*b, lambda a,b: a/b if b != 0 else print("b는 0이 될 수 없습니다.")]
# print(cal_list[3](1,6))

# cal_dict = {'plus': lambda a,b: a+b, 
#             'minus': lambda a,b:a-b,
#             "multiply": lambda a,b:a*b}
# print(cal_dict['plus'](1,2))
# oddOrNot = lambda x: True if x % 2 == 0 else False

# # map 함수: 특정 함수와 반복가능한 자료형을 입력받아, 특정함수가 수행한 결과값을 return
# # 사용예시: map(함수, 리스트(또는 튜플 등등))
# def two_times(x):
#     return x*2
# lst = list(map(two_times, [1,2,3,4]))
# print(lst)

# # map함수와 lambda함수를 사용해서
# # 입력한 list의 제곱값을 담은 list를 출력하도록 하자.

# lst = list(map(lambda x: x**2, [1,2,3,4]))
# print(lst)

# # map의 역할은 대상이 되는 리스트를 가지고, 새로운 리스트를 만들어내는 것이다.
# # filter의 역할은 대상이 되는 리스트에서 특정한 조건으로 값을 걸러내는 것.
# # 함수를 적용하여 특정한 조건으로 값을 걸러내는 것
# def trueOrNot(x):
#     if x > 0:
#         return True
#     else:
#         return False
    
# lst = list(filter(trueOrNot, [-1, 0, 3, -2, 5]))
# print(lst)

# # 위 로직을 labmda를 써서 바꿔보자(삼항연산자)
# # map을 사용하게 되면 True, False 그 자체가 새로운 리스트에 담기게 된다.
# lst = list(filter(lambda x: True if x > 0 else False, [-1,0,3,-2,5]))
# print(lst)

# # 함수형 프로그래밍을 사용하여, 주어진 list에서 홀수만 추출하도록 하여라.
# lista = [4,7,1,2,5,6,8]
# print(lista)
# lst = list(filter(lambda x: True if x % 2 == 1 else False, lista))
# print(lst)

# # sum : 주어진 자료들의 총합
# sum_value = sum(filter(lambda x: True if x % 2 != 0 else False, lista))
# print(sum_value)

# #문자를 아스키코드 변환: ord()
# print(ord('a'))
# # 숫자 107이 의미하는 아스키코드상의 문자는 뭘까? : chr()
# print(chr(97))
# # 예를 들어 문자열이 주어질 때 숫자를 제외하고 문자값만 새로운 문자열로 만들어보아라.
# str1 = '123asdf512kjlk'
# print(ord('z')) # 소문자 a~z : 97~122
# print(ord('A')) # 소문자 a~z : 65~90
# new_str =""
# for a in str1:
#     if (122 >= ord(a) >= 97) or (65 >= ord(a) >= 90):
#         new_str += a
# print(new_str)

# # 절대값 구하기: abs()
# print(abs(-3))
# # map을 사용해서 주어진 리스트를 절대값으로 변환한 리스트를 출력해보자.
# lista = [1,-5,12,-5]
# lst = list(map(abs,lista))
# print(lst)

# 재귀함수
# factorial 예제
# 변수 n을 넣었을 때 n!가 나오도록 함수를 만들어보자.
# def factorial(n):
#     fac =1
#     for a in range(1,n+1):
#         fac *= a 
#     return fac

# print(factorial(3))

# 재귀함수를 통한 factorial 예제
# 재귀함수란 함수 내에서 함수 자기자신을 호출하는 함수.
# 재귀함수에서는 반드시 재귀함수를 종료시키는 조건이 들어가야한다.
# def test(n):
#     if n == 1:
#         return 1
#     return n+test(n-1)

# result = test(10)
# print(result)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)
# result = factorial(4)
# print(result)

# 재귀함수를 반드시 써야만 하는 상황
# 반복의 횟수를 알 수 없을 떄

# 다섯 개의 숫자 중에 2개씩 숫자를 추출하는 경우의 수를 구하고자 한다.

lista = [10,20,30,40,50]
# answer = []
# for a in range(len(lista)):
#     for b in range(a+1,len(lista)):
#         answer.append([lista[a],lista[b]])
# print(answer)

def comb(lista,num,count):
    answer = []
    for a in range(0+count,len(lista)):
        if count  :
            break
        count += 1
        answer.append([lista[a],comb(lista,num,count)])
        
    return answer
a=comb(lista,2,0)

print(a)