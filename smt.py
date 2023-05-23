from z3 import *

# 버블 정렬을 나타내는 불린 변수를 생성.
bubbleSort = Bool('bubbleSort')

n = Int('n')

# 시간 복잡도가 n^2이라는 불린 변수를 생성.
timeComplexN2 = Bool('timeComplexN2')


# SMT Solver를 생성.
s = Solver()


# Sygus에서 나온 것들을 add 할 때 각 원소로 추가하면 된다.
# smt에는 조건식이 이미 추가되어 있다.
# Sygus에서 나온 원소들이 조건식을 만족할 
# 버블 정렬의 조건을 추가.
s.add(bubbleSort)

s.add(timeComplexN2)

s.add(timeComplexN2 == (n * n))


# 버블 정렬이 n^2 시간 복잡도를 가지는 조건을 추가.
s.add(Implies(bubbleSort, And(timeComplexN2, timeComplexN2 == (n * n)))) #오리면 만족



# 이 문제가 만족 가능한지(SAT) 확인하고 결과를 출력.
result = s.check()
if result == sat:
    print("검증 결과: SAT")
    print("이 조건은 버블 정렬을 나타냅니다.")
    print(s.model())
else:
    print("검증 결과: UNSAT")
    print("이 조건은 버블 정렬을 나타내지 않습니다.")
