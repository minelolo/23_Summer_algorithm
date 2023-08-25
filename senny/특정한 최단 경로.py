# 백준 1504 : 다익스트라
# 거의 필사한듯
import sys
import heapq
input = sys.stdin.readline
N, E = map(int, input().split()) # N : 노드 개수, E : 에지 개수
myList = [[] for _ in range(N+1)] #인접 리스트

# 인접 리스트 구현 : 무방향 그래프이므로 append 2번
for _ in range(E):
    a, b, c = map(int, input().split())
    myList[a].append((b, c))
    myList[b].append((a, c))

V1, V2 = map(int, input().split())

def root(start):
    distance = [sys.maxsize] * (N+1) #최단 거리 저장 리스트 : 함수 밖에서 정의하면 오답
    distance[start] = 0 # 최단 거리 리스트 초기화
    q = []
    heapq.heappush(q, (0, start)) #힙에 0과 start 투입
    while q:
        dist, now = heapq.heappop(q) #가장 작은 노드 선택
        # 작은 값으로 업데이트
        if distance[now] < dist:
            continue
        for i in myList[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost #작은 값으로 업데이트
                heapq.heappush(q, (cost, i[0]))
    return distance

# 1, v1, v2일 때의 최단 거리 리스트
one = root(1)
v1_root = root(V1)
v2_root = root(V2)

# 1 > V1 > V2 > N(마지막 노드)
v1_path = one[V1] + v1_root[V2] + v2_root[N]
# 1 > V2 > V1 > N(마지막 노드)
v2_path = one[V2] + v2_root[V1] + v1_root[N]

result = min(v1_path, v2_path)
print(result if result < sys.maxsize else -1)