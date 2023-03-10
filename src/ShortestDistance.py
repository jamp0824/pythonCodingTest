#최단 경로 : 가장 짧은 경로를 찾는 알고리즘 : 길 찾기 문제
# 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
# 최단 경로를 모두 출력하는 문제보다는 단순히 최단 거리를 출력하도록 요구하는 문제
# 다익스트라 최단 경로와 플로이드 워셜 알고리즘 유형

#다익스트라 최단 경로 알고리즘 : 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
#음의 간선이 없을 때 사용 : 0보다 작은 값을 가지는 간선
#그리드 알고리즘 : 가장 바용이 적은 노드
# 출발 노드를 설정한다
# 최단 거리 테이블을 초기화한다
# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다
# 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 위의 과정에서 3번째와 4번째를 반복한다.

# 다익스트라 알고리즘은 최단 경로를 구하는 과정에서 '각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신
# 매번 현재 처리하고 있는 노드와 인접한 노드로 도달하는 더 짧은 경로를 찾으면 '더 짧은 경로도 있었ㅈ네? 이제부터는 이경로가 제일 짧은 경로야" 판단

#따라서 방문하지 않은 노드 중에서 현재 최단 거리가 가장 짧은 노드를 확인'해 그 노드에 대하여 4번째 과정을 수행한다는 점

#한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해

#구현 : 처음에 각 노드에 대한 최단 거리를 담는 1차원 리스트를 선언한다
# 이후에 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)한다.

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
#시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문 하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(index)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    #시작 노드를 제외한 전체 n -1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리의 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now]+j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
        # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])