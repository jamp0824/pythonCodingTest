# 유효 숫자
# 유효숫자e 지수 = 유효숫자 x 10 지수

a = 1e9
print(a)
a = 75.25e1
print(a)
a = 3954e-3
print(a)

#소수 표현 방식
a = 0.3+ 0.6
print(a)
print(round(a,1))

a = 5
b = 3
print(a**b)

#나누기
print(a/b)
#몫
print(a//b)
#나머지
print(a%b)
#리스트 만들기

#빈객체 선언법
a = list()
print(a)

a = [1,2,3,4,5,6,7]
print(a[2]==a[-5]) #true

# 크기가 n이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0]*n
print(a)

a[2] = 4
a[-3] = 2
print(a[1:4]) #[0,4,0]

#리스트 컴프리헨션 : 리스트를 초기화하는 방법

#0 부터 19까지 수 중에서 홀수만 포함되어 있는 리스트
array = [i for i in range(20) if i % 2 == 1]
print('array',array)

array = []
for i in range(20):
    if i % 2 ==1:
        array.append(i)
print('array = ',array)

array = [i*i for i in  range(1,10)]

print('array 3 =',array)

array = []
for i in range(1,10):
    array.append(i*i)
print(array)

#N x M 크기의 2차원 리스트 초기화
N = 3
M = 4
array = [[0]*M for _ in range(N)]
print(array)

#언더바(_)는 무슨 역할일까요?
#반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용한다.
#1 부터 9까지의 자연수를 더할 때 왼쪽 예시처럼 작성하지만, 단순히 "Hello World"를 5번 출력할 때는 , 오른쪽(_)를 무시할 수 없다

summary = 0
for i in range(1,10):
    summary += i
print(summary)

for _ in range(5):
    print("Hello World")


#2차원 리스트를 초기화할때는 반드시 리스트 컴프리헨션을 이용해야 한다. 만약에 다음과 같이 NxM 크기의 2차원 리스트를 초기화한다면 의도와같지 않은 결과를 갖는다

#NxM 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4
array = [[0]*m]*n
print(array)

array[1][1] = 5
print(array)

#분명 값을 넣은 [1][1]말고 전체 1번째 row값의 인덱스가 전부 바뀌었다
# 이는 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식하기 때문이다.

a = [1,4,3]
# n.append() 리스트 원소 삽입 O(1)
# n.sort() 기본 정렬 기능으로 오름차순으로 정렬한다 O(NlogN)
# n.sort(reverse = True) 내림차순으로 정렬한다 .
# n.reverse() 리스트의 원소의 순서를 모두 뒤집어 놓는다. O(N)
# n.insert(삽입할 인덱스, 값) 특정한 인덱스 위치에 가지는 원소를 삽입할 때 사용한다.
# n.count(특정값) 리스트에서 특정한 값을 가지는 데이터 개수를 셀 때 사용한다. O(N)
# n.remove() 특정한 값을 갖는 원소를 제거할때, 값을 가진 원소가 여러개면 하나만 제거한다.