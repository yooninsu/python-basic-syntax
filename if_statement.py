# # if문의 기본 문법
# # else는 optional 요소
# # else 상단에 있는 if 또는 elif에 종속된다.
# # elif도 마찬가지로 elif상단의 if에 종속된다.

# # 숫자를 입력받아서.
# # 90이하면 예각
# # 90이면 직각
# # 91~179 둔각
# # 180 평행

# angle = int(input("각도를 입력하시오"))
# if angle < 90:
#     print('예각입니다.')
# elif angle == 90:
#     print('직각입니다.')
# elif angle < 180:
#     print('둔각입니다.')
# else: 
#     print('평행입니다.')


# # a = int(input('숫자를 입력하시오.'))
# # if a >10:
# #       print("a는 10보다 큽니다.")
# # else:
# #       print("a는 10보다 작습니다.")
# # print("a는 10보다 작습니다.")


# # trueOrFalse = True
# # if trueOrFalse:
# #     print("참입니다")
# # else:
# #     print("거짓입니다")

# cash = int(input("얼마를 가지고 있습니까?"))

# if cash >= 30000:
#     print("택시를 타고 가시오.")
# else:
#     print("걸어가시오.")

# a = 10
# if not (a > 5 and a > 100): #false 구문을 True로 바꿈
#     print('참입니다.')


# # 비트연산이란 2진법의 숫자를 |(or), &(and), ^(xor)등으로
# # cpu내부적으로 계산하는 방식
# # # ex)
# # 1111 & 1000 = > 1000
# # 1111 | 1000 => 1111

# # and는 &와 같고, or는 |와 같고, not은 부정의 의미
# # not True는 False가 되고, not False는 True가 된다.

# print(10 or 1) # 10 출력
# print(10 | 1) # 11 츠력

# # 대입연산자
# a = 10
# # a= a+1 이렇게 표현해도 되고, a += 1 이렇게 표현해도 된다.
# a += 1
# print(a)

# # -=, /=, *=

# # a/=5 => a =2
# print(a/5)

# # 비교연사자 중에 chaining
# # 5 < a < 100 이렇게 표현하거ㅏ나 a>5 and 100<a
# a = 10
# if a > 5 and 100 < a:
#     print("참입니다.")

# a= 10
# if a > 5:
#     print("참입니다.")
# if a > 100:
#     print('참입니다.')
# else:
#     print('거짓입니다.') # 바로 위의 if문에 종속이 되어있음.

# # if문 한줄로 쓰기
# # 코드가 짧고 단숞나 경우에 아래와 같이 한줄로 쓰는 것을 권장.
# # 두줄 이상의 코드를 한줄로 적고 싶으면 ;으로 구분

# a = 10
# if a>10: print('"a는 1보다 큽니다');print("a는 1보다 글쎄....")

# # 조건부표현식(삼항연산자): 간단한 식으로 표현.
# # 먼저, if문의 실행문을 if 문 앞으로, :을 빼고, 한줄로.
# a = 10
# print('A는 10보다 큽니다.') if a >10 else print('A는 10보다 크다.')

# # 실행문을 실행하기 위해 사용한다기 보다는,
# # 참인 경우에 어떤 값, 기짓인 경우에 어떤 값을 쉽게 result에 담기 위해 사용

# result = "A는 10보다 큼" if a > 10 else "A는 10보다 작음"
# if a > 10:
#     result = 'A는 10보다 큼'
# else:
#     result = 'A는 10보다 작음'
# print(result)


# lst = [1,2,3,4,5,6,7,8,9,10]
# n = int(input('숫자 하나를 입력하세요'))
# if n in lst:
#     print('입력하신 숫자는 존재합니다.')
# else:
#     print('리스트에 포함되지 않습니다.')

# 10kg 이상부터 수수료를 내야한다. 수수료는 10의 배수 단위로 10000원씩 증가한다. 

# weight = int(input('짐의 무게를 kg 단위로 입력해주세요'))
# fee = weight // 10 * 10000
# result = '짐의 무게는 %dkg이며 수수료는 %d원입니다.' %(weight, fee)
# print(result)
# # f formatting
# print(f"짐의 무게는 {weight}kg이며 수수료는 {fee}원입니다.")

money = int(input("가진 돈을 입력하시오"))
condition = int(input("배고픔을 예,아니오로 입력하시오"))
if money >= 10000 and condition == '예':
    print('저녁을 사 먹으시오.')
else:
    print('집에 가시오.')

# a와 b가  같은지 비교하는 연사자 is
# 객체타입의 경우에는 메모리 주소를 비교하고
# 숫자, 문자, bool 기본타입의 경우 값을 비교한다.
# 숫자, 문자, bool같은 경우에는 데이터 pool을 만들어서 재활용한다.
# 따라서, 값을 비교할 때 메모리 주소가 아니라, 데이터 poo에서 값을 비교한다.

a = 10 # [10,20]
b = 10 # [10,20] -> 참입니다. 가 출력되지 않음. 값이 같다 하더라 메모리 주소가 다르기 때문에
if a is b:
    print("참입니다.")

a = 10
b = 20
if a == b:
    # pass 시키는 것.(pass를 명시적으로 표현한 것)
    pass
else:
    print("두 값이 다릅니다.")







