#import하고 싶은 모듈이 있으면 import 구문을 사용
# from module_test import module_statements
# from 패키지명 import 파일명 또는 import 패키지명.파일명
# as를 사용하여 약오롣 사용가능
# import module_test.module_statements as ms
# print(ms.plus(10,20))

import class_statements
c1 = class_statements.CalculatorChild()

c1.plus(100)
print(f'module_import의 result : {c1.result}')