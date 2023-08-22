'''
첫째 줄에 건물의 종류 수 N(1 ≤ N ≤ 500)이 주어진다. 다음 N개의 줄에는 각 건물을 짓는데 걸리는 시간과 그 건물을 짓기 위해 먼저 지어져야 하는 건물들의 번호가 주어진다. 
건물의 번호는 1부터 N까지로 하고, 각 줄은 -1로 끝난다고 하자. 각 건물을 짓는데 걸리는 시간은 100,000보다 작거나 같은 자연수이다. 
모든 건물을 짓는 것이 가능한 입력만 주어진다.


1. 입력을 해서 각 건물에 대한 정보 입력
2. 5개를 입력으로 받으면 5개를 출력해야 해서 반복문으로 사이클을 돌리면서 출력시간을 출력해야 함
3. 각 건물은 길이가 최소 2(자기자신과 -1) 에서 n + 1 (소요시간 1 + -1 : 1 + 자기자신을 제외하고 전부 필요할 경우 n -1이니 n-1 + 1 + 1) 그럼 2차원 리스트로 하고 전부 길이를 n + 1로 초기화?
4. 각 리스트마다 -1 앞까지 탐색 -1이 아니면 해당 노드로 이동, 이동해도 -1이 아니면 다시 위로 이동하면서 계속해서 맨앞의 숫자를 더해줌 그리고 더했으면 빼서 이미 통과한 것을 제외??
5. 4과정을 n번 반복해서 출력??? 

아직 햇갈려서 교재에 있는 것 그대로 가져왔습니다

'''

from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  # 진입차수 리스트
selfBuild = [0] * (N + 1)  # 자기자신을 짓는데 걸리는 시간



for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])  # 건물을 짓는데 걸리는 시간
    
    
    index = 1
    while True:  # 인접리스트 만들기
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1  # 진입차수 데이터 저장

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (N + 1)
while queue:  # 위상정렬 수행
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(result[i] + selfBuild[i])