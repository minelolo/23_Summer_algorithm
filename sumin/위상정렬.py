#백준 2252
import sys
from collections import deque

#변수 선언 및 입력
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

#위상정렬
queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    print(node, end='')
    for i in graph[node]:
        if indegree[i] == 1:
            queue.append(i)
        indegree[i] -= 1
