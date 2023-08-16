# 백준 1516
# 교재 필사
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

# 인접 리스트 생성
A = [[] for _ in range(N+1)]
# 진입 차수 리스트 생성
indegree = [0] * (N+1)
# 걸리는 시간
time = [0] * (N+1)

for i in range(1, N+1):
    inlist = list(map(int, input().split()))
    time[i] = (inlist[0]) #자기 자신을 짓는데 걸리는 시간
    index = 1
    while True: #인접 리스트 생성
        preTemp = inlist[index]
        index += 1
        if preTemp == -1: #마지막이라면
            break
        A[preTemp].append(i)
        indegree[i] += 1 #진입차수 1 증가

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0: #진입차수가 0인 노드 선택
        queue.append(i) #선택한 노드 정렬 리스트에 저장

result = [0] * (N+1)
while queue: #정렬 리스트의 요소에 대해
    now = queue.popleft() #마지막 요소 삭제
    for next in A[now]:
        indegree[next] -= 1 #노드의 진입 차수 1씩 빼기
        # 시간 업데이트
        result[next] = max(result[next], result[now] + time[now])
        if indegree[next] == 0: #진입차수가 0인 노드 선택
            queue.append(next)

for i in range(1, N+1):
    print(result[i] + time[i])