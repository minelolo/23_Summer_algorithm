# 백준 1325
# python : 시간초과, pypy3 : 정답
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

# 인접 리스트 초기화
computer = [[] for _ in range(N+1)]

# 인접 리스트 생성
for _ in range(M):
    A, B = map(int, input().split())
    # 순서가 있는 그래프 : B를 해킹하면 A도 해킹할 수 있음
    computer[B].append(A)

# 가장 인접 리스트 요소가 많은 경우 출력 : BFS 이용
def BFS(v):
    cnt = 1
    queue = deque([v])
    visit = [False] * (N+1)
    visit[v] = True
    while queue:
        now = queue.popleft() # 현재 노드 삭제
        for i in computer[now]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)
                cnt += 1
    return cnt

result = []
for i in range(1, N+1):
    result.append(BFS(i))

m = max(result)
for i in range(len(result)):
    if m == result[i]:
        print(i+1, end = ' ')