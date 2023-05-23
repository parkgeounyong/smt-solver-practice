from z3 import *

# 시간 복잡도를 나타내는 정수 변수 생성
n = Int('n')

# 불린 변수 생성
bubbleSort = Bool('bubbleSort')
mergeSort = Bool('mergeSort')
timecomplex= Int('timecomplex')
# SMT Solver 생성
s = Solver()

# 버블 정렬과 병합 정렬의 조건 추가
s.add(Implies(timecomplex==n*n, bubbleSort))
s.add(Implies(timecomplex==n, mergeSort))

#시간 복잡도 추가
s.add(timecomplex==n*n)
s.add(n>1)
# 이 문제가 만족 가능한지(SAT) 확인하고 결과 출력
result = s.check()
if result == sat:
    print("검증 결과: SAT")
    model = s.model()
    print(model)

else:
    print("검증 결과: UNSAT")
    print("주어진 시간 복잡도에 해당하는 정렬을 구분할 수 없습니다.")
