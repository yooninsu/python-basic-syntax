#변수명을 지을 때는 숫자가 먼저 나와서는 안된다.
#변수명 중간에 띄어쓰기, 특수기호등을 일반적으로 쓰지 않는다.  
# 특수부호는 일반적으로 사용하지는 않지만 _ 언더바는 번번히 사용한다.

# str(숫자) -> 문자, int(실수) -> 정수

# 'a'라는 문자를 변수에 저장하게 되면, 메모리상에 어떤 숫자값으로 저장될까?
x = 'a'
print(ord(x)) 

# 아스키 코드란 개발자들과 사용자 간의 문자를 숫자로 표현하는 테이블 -> UTF-8

# multi line으로 문자열을 표현하고 싶으면, 쌍따옴표 3개를 사용하거나 홑따옴표 3개를 사용하면 된다.
# 이스케이프문을 활요한 줄바꿈
# 이스케이프문이란 \n 또는 \t 등의 특수기호를 말한다.
a= "hello \nworld"
print(a)
# 역슬래시의 또다른 활용 : 특수문자를 있는 그대로 표현하는 역할
# "쌍따옴표("")는 파이썬에서 문자를 의미한다"라는 문구를 출력해보세요.
c= "쌍따옴표 (\")는 파이썬에서 문자를 의미한다"
print(c)
b="python's easy"
print(b)

# 문자열 더하기, 곱하기
# a라는 변수에 python이라는 문자열을 담고, b라는 변수에는 is fun이라는 문자열을 담는다. 그리고 c라는 변수에 두 문자열을 더한 값을 넣어 c를 출력
a= 'python'
b= ' is fun'
c= a+b
print(c)
# 문자열 곱하기
# python python is fun 출역
print(a*2+b)

# 파이썬에서 인덱스란, 기본적으로 특정위치를 가리키는 용도로 사용
#인데스의 사용방법은 원하는 대상 [숫자값]
# 0,1,2,3,4,5...의 체계
a = "python's fun"
print(a[3])

# 문자열의 마지막 문자를 출력해보자.
a = "python's fun python's fun python's fun"
print(a[-1])
print(a[len(a)-1])

# 문자열의 슬라이싱
# 슬라이싱이란 문자열을 잘라내는 것을 의미
# 대상변수[x:y] : x이상 y미만의 index를 가진 문자열을 잘라낸다.
a = "python is fun"
# python만 잘라내서 b에 담아 출력해주세요
b= a[0:6]
print(b)
# x, y 자리에 값이 없으면 처음부터 또는 끝까지를 의미
# 6번째 문자부터 끝까지 잘라내서 변수 c에 담아 출력
c = a[6:]
print(c)
# a[x:y:z] 여기에서 z는 z-1 개씩 건너뛰고
# 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력.
b = a[2:7:2]
print(b)

#연습문제(슬라이싱)
# A = 20220505children's_day 슬라이싱을 이용하여 date라는 변수에 날짜, day라는 변수에 children's_day를 담아서 각각 출력하시오.
A = "20220505children's_day"
date = A[:8]
day = A[8:]
print(date)
print(day)

# 문자열 포맷팅이란 문자열 중간에 

myage = int(input("나이를 입력하시오: "))
myweight = float(input("몸무게를 입력하시오:"))
myinfo = "my age is %d, and weight is %f kg" %(myage ,myweight)
print(myinfo)



