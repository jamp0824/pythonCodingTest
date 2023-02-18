
#파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.
#permutations combinations

#permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든
#경우(순열)를 계산해준다. 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
#리스트['A','B','C'] 에서 3개(r=3)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다.

from itertools import permutations

data = ['A','B','C'] # 데이터 준비
result = list(permutations(data,3)) #모든 순열 구하기

print('permutations',result) #[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형을 변환하여 사용한다.
# 리스트['a','b','c']에서 2개를 (r =2)를 뽑아 순서와 상관없이 나열하는 모든 경우를 출력하는 예시

from itertools import combinations

result = list(combinations(data,2)) #2개를 뽑는 모든 조합을 구하기
print('combinations',result)  #[('A', 'B'), ('A', 'C'), ('B', 'C')]

#product는 permutations와 같은 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다.
#다만 원소를 중복으로 뽑는다. product객체를 초기화할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.
#product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다. 리스트['a','b','c']에서 중복을 포함하여
# 2개 (r = 2)를 뽑아 나열하는 모든 경우를 출력하느 예시는 다음과 같다.

from itertools import product

result = list(product(data, repeat = 2)) # 2개를 뽑는 모든 순열 구하기 (중복허용)
print('product',result)

#combinations_with_replacement 는 combinations와 같은 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고
#나열하는 모든 경우(조합)를 계산한다. 다만 원소를 중복해서 뽑는다. combinations_with_replacement는 클래스이므로 객체 초기화 이후에는
#리스트 자료형으로 반환하여 사용해야한다. 리스트['a','b','c']에서 중복을 포함하여 2개(r = 2)를 뽑아 순서와 상관없이 나열하는 모든
#경우를 출력하는 예시는 다음과 같다.

from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data,2))
print('combinations_with_replacement',result)

