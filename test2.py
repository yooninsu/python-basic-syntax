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


# participant = ["mislav", "stanko", 'mislav',"mislav", "ana"]	
# completion = ['stanko','mislav', 'ana','mislav']

# #completion을 dict로 변환
# # participant를 for 문으로 1개씩 꺼내서 completion[p] = completion[p] -1

# dictc ={}
# for c in completion:
#   if c not in dictc.keys():
#       dictc[c] = 1  
#   else:
#      dictc[c] = dictc[c] + 1
# for p in participant:
#   if p in dictc.keys() and dictc[p] > 0:
#     dictc[p] = dictc[p] -1
#     print(p)
#   else:
#      answer = p
# print(answer)
   
      
# answer = ''
# for a in participant:
#     if a in completion:
#         completion.remove(a)
#     else:
#         answer = a
# return answer

# 가운데 글자 뽑기
# s = "qwer"
# for a in s:
#   if len(s) %2 == 1: 
#      answer = s[len(s) // 2]    
#   else:
#       answer = s[int(len(s)//2)-1:int(len(s)//2)]
# print(s[1:2])
# print(answer)

arr = [4,3,2,1]
templist = arr[:]
answer = []
min = arr[0]
for a in range(len(arr)):
  if min <= arr[a]:
    templist.remove(arr[a])
  else:
    min = arr[a]  
  answer.append(min)
print(answer)

