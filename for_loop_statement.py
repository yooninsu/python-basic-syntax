# while문의 기본구조
# a = 0
# while a  < n:
#   실행문
# a +=1
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
# import random
# print(random.randint(1,45))
# # 리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또번호를 만들어보자.
# lotto = []
# a = 0
# while a < 6:
#     num = random.randint(1,45)
#     lotto.append(num)
#     a +=1
# print(lotto)




# for 문의 기본 구조
# for 변수 in 반복가능한자료형
# 실행문
# lista = [1,2,3,4,5,6,7,8,9,10]
# for a in lista:
#     print(a)

# # range 문법: range(x,y) x이상 y미만
# # for a in range(1,101):
# #     print(a)
# # range의 의미: iterable 객체
# v1 = list(range(1,10))
# print(v1) #[1,2,3,4,5,6,7,8,9]

# #range(x,y): x이상 y미만의 숫자를 담은 객체
# #range(y): 0이상 y미만의 숫자를 담은 객체

# v1 = list(range(10,20))

# # for a in 리스트를 써서 v1의 값을 모두 출력
# for a in v1:
#     print(a)

# # for a in range를 써서 v1[index]의 형태로 v1의 값을 모두 출력
# for a in range(len(v1)):
#     print(v1[a])

# # for a in 리스트 구문으로는 원본리스트 데이터를 변경할 수 없다.
# lista = [10,20,30,40,50,60,70,80,90,100]
# for a in lista:
#      a = 100 # 이런 방식으로는 원본의 lista의 값을 변경할 수 없다.
# #lista[5] = 100 리스트의 5번째 인덱스의 값을 변경하는 방법.

# # 직접 리스트의 index로 접근해야지 원본을 바꿀 수 있다.
# for a in range(len(lista)):
#     lista[a] = 100
# print(lista)


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


# 리스트를 만드는 방법 중에 list comprehension이라는 방법이 있다.
# 리스트에 0~9까지를 담는 방법
# # method1
# lista = [0,1,2,3,4,5,6,7,8,9]
# # method2
# lista = list(range(10))
# # method3 홀수인 값에 2를 곱한 값만을 list로 만들어라
# lista = []
# for a in range(10):
#     if a % 2 == 1:
#         lista.append(a*2)
# print(lista)
# # method4: list comprehension
# # 장점: 간결하다.
# lista = [pow(a,2) for a in range(10) if a % 2 ==1]
# print(lista)

# # 한 반에 수학점수가 60점이 넘으면 합격, 60점 미만이면 불합격.
# lista = [90,25,67,45,80]
# #위의 리스트가 학생의 번호순서대로 있을 때, 아래와 같이 출력하시오.
# #1번 학생은 합격입니다.

# count = 1
# for a in lista:
#     if a >= 60:
#         print(f'{count}번 학생은 합격입니다.')
#     else:
#         print(f'{count}번 학생은 불합격입니다.')
#     count += 1

# # range 사용
# for a in range(len(lista)):
#     if lista[a] >= 60:
#      print(f'{a+1}번 학생은 합격입니다.') 
#     else:
#         print(f'{a+1}번 학생은 불합격입니다.')
    

# for문과 break : for문에서 break문을 반드시 써야 하는 상황
# 선착순 1명만 찾는 상황.

# 혈액형이 a형인 고객 선착순 1명만 찾는 상황.
# lista = ['b', 'b', 'ab', 'a', 'b', 'a']
# 출력결과: 4번째 고객이 이벤트에 당첨되었습니다.

# num = 1
# while num <= len(lista):
#     if lista[num-1] == 'a':
#         break
#     num +=1
# print(str(num) + "번째 고객이 이벤트에 당첨되었습니다.")


# for 문을 이용한 구구단
# 구구단 5단을 출력해보자.
# five = 5
# for n in range(1,10):
#     print(f'{five}X{n}={five*n}')
# 구구단 몇단을 계산해드릴까요?

# while True:
#     num = int(input("구구단 몇 단을 계산해드릴까요?"))
#     for a in range(1,10):
#         print(f'{num}X{a}={num*a}')
#     continue

# 2중 for문
# 구구단을 5~9단까지 한꺼번에 출력

# for a in range(5,10):
#     for n in range(1,10):
#         print(f"{a}X{n}={a*n}")

# lista = [10,20,30,40]
# # lista[0]와 lista[1]의 자리를 바꾸려면?
# # lista =[20,10,30,40]
# temp = lista[0]
# lista[0] = lista[1]
# lista[1] = temp
# print(lista)
# # 파이썬에서 지원하고 있는 문법
# lista[0], lista[1] = lista[1], lista[0]
# print(lista)

# for문을 이용한 정렬 알고리즘

# # 선택정렬
# lista = [93,45,21,30,20,94,66,71,45]

# # 위 리스트를 어떻게 오름차순 정렬 할 것인가?
# for a in range(len(lista)-1): # range를 쓰는 이유는 인덱스 값을 접근하기 위해서 (첫번쨰 for문은 채워나가야할 index를 의미)
#     for b in range(a+1,len(lista)): # 두번째 For문은 비교의 대상이 되는 index를 의미
#         if lista[a] > lista[b]:
#             temp = lista[a]
#             lista[a] = lista[b]
#             lista[b] = temp
# print(lista)


# # 버블정렬
# for a in range(len(lista)):
#     for b in range(len(lista)-a-1):
#         if lista[b] > lista[b+1]:
#             temp = lista[b]
#             lista[b] = lista[b+1]
#             lista[b+1] = temp
# print(lista)

# # 행렬의 합
# arr1 =[[1,2],[2,3],[1,2,5]]
# arr2 = [[3,4],[5,6],[1,2,5]]
# answer = []
# for a in range(len(arr1)):
#     temp = []
#     for b in range(len(arr1[a])):
#         temp.append(arr1[a][b]+arr2[a][b])
#     answer.append(temp)
# print(answer)

# # 행렬의 곱
# arr1 = [[1, 4], [3, 2], [4, 1]]
# arr2 = [[3, 3], [3, 3]]
# answer = []
# for a in range(len(arr1)):
#     temp = []
#     for b in range(len(arr1[a])):
#         temp.append(arr1[a][b]*arr2[a][b])
#     answer.append(temp)
# print(answer)

