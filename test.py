my_string = 'bread'
# 방법 1: list로 변환 후 reverse
stlist = list(my_string)
stlist.reverse()
answer = "".join(stlist)
print(answer)
# 방법 2: slicing
answer = my_string[::-1]
# 방법 3: reversed(문자열)
answer = "".join(reversed(my_string))
print(answer)

# #배열 원소의 길이
# strlist = ["We", "are", "the", "world!"]
# answer = []
# for i in range(0,len(strlist)):
#     lista = strlist[i].split()
#     stra = "".join(lista)
#     listb = len(stra)
#     answer.append(listb)
# print(answer)
# # method 2
# answer =[]
# for i in strlist:
#   answer.append(len(i))
# print(answer)

# # 점의 위치 구하기
# answer = 0
# dot = [1, -32]
# if dot[0] > 0 and dot[1] > 0 :
#   answer = 1
# elif dot[0] < 0 and dot[1] > 0:
#   answer = 2
# elif dot [0] > 0 and dot [1] < 0:
#   answer = 3 
# else:
#   answer = 4 
# print(answer)

# 숫자 문자열과 영단어
# s = "one4seveneight"
# l = ""
# dict1 = {'zero' : 0, "one" : 1, "two" : 2, "three" : 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
# for a in range(len(s)):
#     if not str.isdigit(s[a]):
# 자릿 수 더하기

# n =123
# num = 0
# answer = 0
# lst = [int(a) for a in str(n)]
# for a in lst:
#     answer += a
# print(answer)
# print(lst)

