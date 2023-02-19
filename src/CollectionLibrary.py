#Collection라이브러리는 표준 라이브러리이다. deque와 Counter
# 보통 파이썬은 deque를 이용하여 큐를 구현한다. 별도로 제공하는 QUeue 라이브러리가 있는데
#ㅣ일반적인 큐 자료구조를 구현하는 라이브러리는 아니다. 따라서 deque를 이용해 큐를 구현한다.
#데이터 삽입, 삭제 등 다양한 기능을 제공한다. 리스트가 있을 때 중간에 특정한 원소를 삽입하는 것도 가능하다.
#하지만 리스트 자료형은 append() 메서드로 데이터를 추가하거나 pop() 메서드로 데이터를 삭제할 때
#'가장 뒤쪽 원소'를 기준으로 수행한다. 따라서 앞쪽에 있는 언소를 처리할 때에는 리스트에 포함된 데이터 개수에 따라서
#많은 시간이 소요될 수 있다. 리스트 앞쪽에 있는 원소를 삭제하거나 새 원소를 삽입하는 시간 복잡도는 O(N)이다

#deque 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다. 다만 연속적으로 나열된 데이터의 시작부분이나
#끝 부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적으로 사용될 수 있다.
#deque는 스택이나 큐의 기능을 모두 포함한다고 볼 수 있기 때문에 스택 혹은 큐 자료구조의 대용으로 사용될 수 있다.

#deque는 첫 번째 원소를 제거할 때 popleft()를 사용하며 append()를 사용하고 원소를 삭제할 때에는 popleft()를 사용하면 된다.
#그ㅓ면 먼저 들어온 원소가 항상 먼저 나가게 된다

from collections import deque

data =  deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list[data])

#파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다. 구체적으로 리스트와 iterable 객체가 주어졌을 때
#해당 객체 내부의 원소가 몇 번씩 등장했는지 알려준다.
#따라서 원소별 등장 횟수를 세는 기능이 필요할 때 짧은 소스코드로 이를 구현할 수 있다.

from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict[counter])