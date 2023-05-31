# my_string = 'bread'
# # 방법 1: list로 변환 후 reverse
# stlist = list(my_string)
# stlist.reverse()
# answer = "".join(stlist)
# print(answer)
# # 방법 2: slicing
# answer = my_string[::-1]
# # 방법 3: reversed(문자열)
# answer = "".join(reversed(my_string))
# print(answer)

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




# lista = ['a', 'e', 'i', 'o', 'u']

# st = "huuuuu"
# stList = list(st)

# for문이 돌때마다 stList목록을 갱신
# index out range 안나는 이유는 
# for s in stList:
#   if s in lista:
#     stList.remove(s)

# print(stList)

# dict1 = {}
# count = 1
# for a in lista:
#     if a not in dict1.keys():
#        dict1[a] = count
#     elif a in dict1:
#        count += 1
#        dict1[a] = count
#     count = 1
# print(dict1)


participant = ["mislav", "stanko", 'mislav',"mislav", "ana"]	
completion = ['stanko','mislav', 'ana','mislav']

#completion을 dict로 변환
# participant를 for 문으로 1개씩 꺼내서 completion[p] = completion[p] -1

dictc ={}
for c in completion:
  if c not in dictc.keys():
      dictc[c] = 1  
  else:
     dictc[c] = dictc[c] + 1
for p in participant:
  if p in dictc.keys() and dictc[p] > 0:
    dictc[p] = dictc[p] -1
    print(p)
  else:
     answer = p
print(answer)
   
      




# answer = ''
# for a in participant:
#     if a in completion:
#         completion.remove(a)
#     else:
#         answer = a
# return answer
