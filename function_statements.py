a = 100
# 특정한 input 값이 있을 때, 
# 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
# 그런데, 해당 연산은 매번 빈번하게 사용이 된다고 가정하자.
#
# 복잡 로직의 연산을 함수화 시켜서 재사용할수 있게 해보자.
# input값이 있어도 되고, 없어도 된다.
# return 값이 있어도 되고, 없어도 된다.
def myFunc(myInput):
    calc = (((myInput + 10) * 20) / 10 ) ** 2
    return calc
result2 = myFunc(200)

# 함수명 myPlusFunc
# 함수의 로지은 사용자의 input을 받아 input값의 누적합을 더하라.
def myPlusFunc(input):
    total = 0
    for a in range(1,input+1):
        total += a
    return total
result = myPlusFunc(10)

# input값을 2개를 받아 2값을 더한뒤, *2만큼 하여 reutrn하는 함수를 만들어보자
# 그리고, 해당 함수를 호출하여 호출된 결과갑승ㄹ result에 담아 출력해보자.
def myFunc2(input1,input2):
    total = 2 * (input1 + input2)
    return total
a = myFunc2(10,20)
print(a)
 
# list의 index 함수를 쓰지 않고,
# for문 또는 whilie문을 통해 몇 번쨰 인덱스에 있는 값인지
# print 해보자
lista = [1,4,6,9]

def myIndex(num,llist):
    result = -1 # 값이 없으면 -1이 나오
    for a in range(len(llist)):
        if num == llist[a]:
            result = a
            break # 넣지 않으면 인덱스 함수와 달리 중복되는 경우 계속해서 뒤에 같은 숫자를 찾아낸다.
    return result
# 위의 for문을 활용하여 myIndex라는 이름의 함수를 만들고자 한다.
# input값이 2개(list,찾고자 하는 값), print는 함수 내에서 하지않고, return에 값을 담는다.
print(myIndex(9,[1,2,3,4,5,6,7,8,9,0,12,3,14]))

