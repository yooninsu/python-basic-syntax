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

#배열 원소의 길이
strlist = ["We", "are", "the", "world!"]
answer = []
for i in range(0,len(strlist)):
    lista = strlist[i].split()
    stra = "".join(lista)
    listb = len(stra)
    answer.append(listb)
print(answer)
# method 2
answer =[]
for i in strlist:
  answer.append(len(i))
print(answer)

# 점의 위치 구하기
answer = 0
dot = [1, -32]
if dot[0] > 0 and dot[1] > 0 :
  answer = 1
elif dot[0] < 0 and dot[1] > 0:
  answer = 2
elif dot [0] > 0 and dot [1] < 0:
  answer = 3 
else:
  answer = 4 
print(answer)