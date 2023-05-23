#대소문자 변경: upper()/ lower()

a = "HelLo"
print(a.upper())
print(a.lower())

# 문자열 양쪽 공백을 없애는 함수: strip()

a = "  hello world   "
print(a.strip())

# 문자열 대체: replace()
a = 'I studied python'
print(a.replace('python', 'java'))

# 공백을 기준으로 문자를 자르는 함수: split()
a = "I studied python"
b = a.split()
print(b)

a = "I    studied   python"
b = a.split(" ")
c = a.split()
print(b)
print(c)

a = "I:studied:python"
b = a.split(":")
print(b)

#연습문제(숫자형)
#아래와 같은 2차 방정식을 파이썬 수식으로 코딩하고 y의 결과를 출력하라.
x = int(input("숫자를 입력하시오:"))
Y = 2.5*pow(x,2)+3.3*x+6
print(Y)

