# 내장함수 print(). input 같은 기본 입출력 기능부터 sorted()와 같은 정렬기능을 포함하고 있는 내장 라이브러리이다.
# itertools : 파이썬에서 반복되는 형태를 데이터를 처리하는 기능을 제공하는 라이브러리이다. 순열과 조합 라이브러리를 제공한다.
# heapq: 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.
# bisect : 이진 탐색(Binary Search ) 기능을 제공하는 라이브러리이다.
# collection: 덱(deque), 카운터(Counter)등의 유요한 자료구조를 포함하고 있는 라이브러리이다.
# math : 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함하고 있다.

#내장함수
result = sum([1,2,3,4,5])
print('result = ',result)

#min 함수는 파라미터가 2개이상 들어왔을 때 작은 값을 반환한다.
result = min([2,10,3,1])
print('result = ',result)

result = max([100,23,41,1])
print('resut = ',result)

#eval 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다. 예를 들면
result = eval("(3+5)*7")
print(result)

#sored()함수는 iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다. key 속성으로 정렬 기준을 명시할 수 있으며 reverse 속성으로 정렬된 결과 리스트를
#뒤집을지의 여부를 설정할 수 있다.
result = sorted([9,1,8,5,6])
print('result = ',result)
result = sorted([9,1,8,5,6], reverse = True)
print('result reverse = ',result)

#정렬 기준을 key 속성을 이용해 명시 할 수 있따. 예를 들어 아래와 같은 리스트가 있을 때 두번째 원소(수)를 기준으로 내림차순을 정렬하고자 한다면
result= sorted([('홍길동',75),('이순신',90),('장영실',80)], key= lambda x: x[1], reverse=True)
print(result)

#리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있어 굳이 sorted() 함수를 사용하지 않고도 sort() 함수를 사용해 정렬할 수 있다.
#이 경우 리스트 객체의 내부 값이 정렬된 값으로 바로 변경된다
data = [9,1,5,3,6]
data.sort()
print('data',data)

