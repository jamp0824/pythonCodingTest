#이진 탐색을 쉽게 구현할 수 있는 bisect 라이브러리이다.
#정열된배열에서 특정한 원소를 찾아야할떄 매우 효과적이다. bisect 라이브러이에서는 bisect_lect() 함수와 bisect_right()함수가
#가장 중요하게 사용되며 이것은 시간복잡도 O(logN)에 동작한다.

#bisect_left(a,x) 정렬된 수서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
#bisect_right(a,x) : 가장 오른쪽 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

#또한 정렬된 리스트에서 가장 값이 특정 범위에 속하는 원소의 개수를 구하고자할때 효과적으로 사용할 수 있다.
#아래의 count_by_range(a,left_value,right_value) 함수
#정렬된 리스트 값이 에 속하는 데이터 개수를 반환한다.
#원소 값을 x라고 할때 lef_value<=x<=right_value인 원소의 개수를  O(logN)으로 빠르게 계산할 수 있다.

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    print('right = ',right_index)
    left_index = bisect_left(a,left_value)
    print('left = ',left_index)
    return right_index - left_index

#리스트 선언
a = [1,2,3,3,3,3,4,4,8,9]

#값이 4인 데이터 개수 출력
print(count_by_range(a,-1,3))