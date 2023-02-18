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
a.append(4)
print(a)
# n.sort() 기본 정렬 기능으로 오름차순으로 정렬한다 O(NlogN)
a.sort()
print(a)
# n.sort(reverse = True) 내림차순으로 정렬한다 .
a.sort(reverse = True)
print(a)
# n.reverse() 리스트의 원소의 순서를 모두 뒤집어 놓는다. O(N)
a.reverse()
print(a)
# n.insert(삽입할 인덱스, 값) 특정한 인덱스 위치에 가지는 원소를 삽입할 때 사용한다. O(N)
a.insert(1,7)
print(a)
# n.count(특정값) 리스트에서 특정한 값을 가지는 데이터 개수를 셀 때 사용한다. O(N)
print('count for value 4 in array = ',a.count(4))
# n.remove() 특정한 값을 원소를 제거하는데 값을 가진 원소가 여러개면 하나만 제거한다. O(N)
a.remove(4)
print('specific num of 4 in array is removed = ',a)

#append 대신에 insert를 남발하면 시간복잡도가 높아지기 때문에 시간 초과로 테스트 못통과한다
#2개이상의 원소 삭제
remove_set = [7,4]

result = [i for i in a if i not in remove_set]
print(result)