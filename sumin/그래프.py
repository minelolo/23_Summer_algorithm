#백준 18352
import sys
from collections import deque

input = sys.stdin.readline
#변수 입력 받기
N, M, K, X = map(int, input().split())
#그래프 생성
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
answer = []

#BFS 함수
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        nownode = queue.popleft()
        for i in range(graph[nownode]):
            if visited[i] == 0:
                visited[i] = visited[nownode] + 1
                 queue.append(i)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

BFS(X)

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
