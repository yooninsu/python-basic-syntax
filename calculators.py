import math
#제곱, 제곱근
#2의 10제곱을 출력하라
print(2**10)
print(pow(2,10))
print(math.pow(2,10))
# 1024의 제곱근을 구하라
# 제곱근은 math라는 라이브러리를 import해줘야한다.
print(math.sqrt(1024))

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
a = "python's fun"
print(a[3])
