# while문의 기본구조
# while 조건식: # 조건식이 참인 경우 반복 => 무한반복이 기본 전제.
# # 실행문
# a = 10
# while a > 5:
#     print("참입니다.")

# 조건을 체크 후 True이면 실행문을 1회 실행시키고,
# 다시 조건을 체크하러 돌아온다. 그리고 True이면 또 다시 실행.
# 그러다, 조건이 False되면 while문 종료.

# a = 5
# while a > 0:
#     print(str(a)+'번 반복')
#     a -= 1

# 1~1000 까지만 출력
# a = 1 
# sum = 0
# while a <=1000:
#     print(a)
#     a +=1
# print(sum)

# while 문에서 반복을 진행하다가 break를 만나면, 반복문 종료
# 1)if 문을 써서 xxx한 조건에 break

# a = 1
# sum = 0
# while True:
#     sum += a
#     if a > 1000:
#         break
#     a += 2
# print(sum)

# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동.
# 아래와 같이 코딩하면 hello가 무한 출력

# a = 0
# while a < 1000:
#     print('hello')
#     continue
#     a += 1

# 2) 1~1000 중에 홀수만 더해서 출력
# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동.
# a = 0
# sum = 0
# while a <1000:
#     a += 1
#     if a % 2 == 0:
#         continue
#     else:
#         sum += a
#         # continue 문을 활용해서 coding.
# print(sum)


# while True:
#     num1 = int(input("1~180까지 입력해주세요"))
#     if num1 > 180:
#         print('잘못된 값입니다.') 
#         continue   #불필요한 로직을 수행하지 않고 다시 조건으로 이동할 수 있게 해준다.
#     if num1 < 90:
#         print('예각입니다.')
#     elif num1 == 90:
#         print('직각입니다.')
#     elif num1 < 180:
#         print("둔각입니다.")
#     elif num1 == 180:
#         print('평행입니다.')

# 로또 번호 생성기
# 랜덤의 값을 추출하는 파이썬 라이브러리 -> random
import random
print(random.randint(1,45))
# 리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또번호를 만들어보자.
lotto = []
a = 0
while a < 6:
    num = random.randint(1,45)
    lotto.append(num)
    a +=1
print(lotto)




# for 문의 기본 구조
# for 변수 in 반복가능한자료형
# 실행문
# lista = [1,2,3,4,5,6,7,8,9,10]
# for a in lista:
#     print(a)

# range 문법: range(x,y) x이상 y미만
# for a in range(1,101):
#     print(a)

# ll = []
# while True:
#     num1 = int(input("리스트의 크기를 입력해주세요"))
#     if num1 > 10:
#         print("리스트 크기를 10이하로 다시 할당하세요.")
#         continue
#     for a in range(num1):
#         num=int(input("리스트 값을 할당해보세요:"))
#         ll.append(num)
#     print(f'크기 {num1}의 리스트 {ll}가 할당 되었어요.')



