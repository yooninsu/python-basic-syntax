# method1
order = 2467185687738216378138461823
answer = 0
for a in ['3','6','9']:
    answer += str(order).count(a)
# method 2
for a in list(str(order)):
    if a in ['3','6','9']:
        answer += 1
print(answer)