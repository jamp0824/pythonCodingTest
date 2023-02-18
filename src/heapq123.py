#다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에 우선순위 큐를 구현하고자 할 때 사용한다.
#PriorityQueue 라이브러리도 있지만 heapq가 더빠르다
#파이썬은 최소 힙min heap이 구성되어 있으므로
# 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완성된다.
#보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은'원소이기 때문이다.

#힙에 원소를 삽입할때는 heapq.heappush() 메서드를 이용하고, 힙에서 원소를 꺼내고자할떄는 heapq.heappop()를 이용한다.
#힙 정렬을 heapq로 구현하는 예제를 heapq의 사용방법을 해보자
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,4,7,3,7,4,3,2])
print(result)

#파이썬은 최대 힙을 제공하지 않는다. 따라서 heapq 라이브러리를 이요해 최대힙을 구현해야 할때는 원소의 부호를 임시로 변경하는
#방식을 사용한다. 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가 다시 원소의 부호를 바꾸면 된다. 이러한 방식으로
#최대 힙을 구현하여 내림차순 정렬을 구현해보자

def heapsort2(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort2([1,5,2,7,8,4])
print(result)