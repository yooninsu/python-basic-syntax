# 클래스의 사용
# 1) 같은 기능의 함수의 집합
# 2) 객체를 만들기 위해 사용

# 사칙연산 함수가 있을 떄, 같은 기능을 하므로
# Calculator이라는 클래스에 모아둘 수 있다.
# 명명규칙: 일반적으로 class는 대문자 알파벳으로 시작
# 변수명, 함수명은 소문자로 시작 -> camalcase
# 함수의 집합으로서의 클래스 -> 일반적이지 않은 형태

# class Calculator:
#     result = 0
#     def plus(a,b):
#         return a+b
#     def minus(a,b):
#         return a-b
#     def multiply(a,b):
#         return a*b
#     def divide(a,b):
#         return a/b 
# print(Calculator.plus(10,20))



class Calculator:
    result = 0
    # 클래스 변수 접근가능 방법1: 클래스명.변수
    # 방법2: classmethod 데코레이터 사용
    # class내에 선언된 함수는 매서드라 부른다.
    @classmethod # 사용하면 함수가 처음 받는 변수를 class로 인식
    def plus(cls,a):
        cls.result += a
    def minus(a):
        Calculator.result -= a
    def multiply(a):
        Calculator.result *= a
    def divide(a):
        Calculator.result /= a 
print(Calculator.result)
Calculator.plus(10)
print(Calculator.result)
Calculator.minus(5)
print(Calculator.result)
# 위 클래스의 문제점은 클래스 내에서 누적된 값을 변수로 갖고 있지 않다.

# 객체란 클래스의 복제본, 인스턴스라 부르기도 한다.
# 객체의 사용 이유
# 클래스의 중복 제거 : 변수와 함수의 재활용의 어려움 해결
# 객체 형식의 클래스의 기본 구조
class Calculator:
    # 객체가 생성될때 init은 가장 먼저 실행
    # __init__이란 생성자: 생성자는 객체 생성될 때 객체 변수를 초기화.
    # result와 self.result는 다른 값이다.
    def __init__(self,result):
        self.result = result
    # 객체를 만들 때 클래스 내의 함수의 매개변수가 2개 이상이면
    # 클래스 내의 함수의 매개 변수가 2개 이상일 때, 첫번째 매개변수는 객체를 의미한다.
    def plus(self,a):
        self.result += a
    def minus(self,a):
        self.result -= a
    def multiply(self,a):
        self.result *= a
    def divide(self,a):
        self.result /= a

aCompany = Calculator(1000)
aCompany.plus(100)
bCompany = Calculator(500)
bCompany.plus(100)
print(aCompany.result)
print(bCompany.result)

# Person이라는 클래스를 만든다.
# 생성자로 이름(name), 나이(age), 성별(gender), email을 받아 각각의 객체변수를 만든다.
# register이라는 매서드를 만들어서, 해당 메서드에서는 myinfo라는 객체변수에 이름, 나이, 성별, email 정보를 문자열로 담는다.
# 2명의 person을 만든다.
# print(p1.myInfo)
# print(p2,myInfo)
import datetime

# class Person:
#     def __init__(self,name,age,gender,email):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.email = email
#         self.regDate = datetime.today()
#     def register(self):
#         self.myInfo = self.name+ " " + self.age+ " " + self.gender+ " " + self.email+ " " + str(self.regDate)

# p1 = Person("길동","27","male","gildong@naver.com")
# p2 = Person("춘자","24","female","chunja@gmail.com")
# p1.register()
# p2.register()
# print(p1.myInfo)
# print(p2.myInfo)

# init을 깡통으로 해서 사용할 때

class Person:
    def register(self,name,age,gender,email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.regDate = datetime.datetime.now()
        self.myInfo = self.name+ " " + self.age+ " " + self.gender+ " " + self.email+ " " + str(self.regDate)

p1 = Person()
p2 = Person()
p1.register("길동","27","male","gildong@naver.com")
p2.register("춘자","24","female","chunja@gmail.com")
print(p1.myInfo)
print(p2.myInfo)

