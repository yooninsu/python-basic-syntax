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

# #연습문제(숫자형)
# #아래와 같은 2차 방정식을 파이썬 수식으로 코딩하고 y의 결과를 출력하라.
# x = int(input("숫자를 입력하시오:"))
# Y = 2.5*pow(x,2)+3.3*x+6
# print(Y)

#연습문제(문자열)
# 3개의 단어를 키보드로 입력 받아 각 단어의 첫 글자를 추출 후 단어의 약자를 출력하라.
w1 = input('단어를 입력하시오')
w2 = input('단어를 입력하시오')
w3 = input('단어를 입력하시오')
abbr = w1[0]+w2[0]+w3[0]
print(abbr)