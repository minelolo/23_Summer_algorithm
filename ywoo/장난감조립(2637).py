'''
예를 들어보자. 기본 부품으로서 1, 2, 3, 4가 있다. 중간 부품 5는 2개의 기본 부품 1과 2개의 기본 부품 2로 만들어진다. 
그리고 중간 부품 6은 2개의 중간 부품 5, 3개의 기본 부품 3과 4개의 기본 부품 4로 만들어진다. 마지막으로 장난감 완제품 7은 2개의 중간 부품 5, 
3개의 중간 부품 6과 5개의 기본 부품 4로 만들어진다. 이런 경우에 장난감 완제품 7을 만드는데 필요한 기본 부품의 개수는 1번 16개, 2번 16개, 3번 9개, 4번 17개이다.

1. 각 부품은 어떤 부품간의 결합으로 만들어지는 것을 확인하기 위해서 인접 리스트 구현
2. 인접 리스트를 구현했다면 이를 통해서 어떤 제품이 만들어지는 지를 재귀를 통햏서 구현??



'''



import sys
from collections import deque
input=sys.stdin.readline
#입력값 받기 
N=int(input()) #부품 수 N이 완제품
V=int(input()) #간선 수
E=[[] for _ in range(N+1)] #연결정보.
indegree=[0]*(N+1) #부품별 진입차수 0일 경우 기본부품.
needs=[[0]*(N+1) for _ in range(N+1)] #각 부품이 기본부품 얼마나 필요한지 Matrix

for i in range(V):
    a,b,c = map(int,input().split())
    E[b].append([a,c])  #a만드는데 b가 c개 필요.
    indegree[a]+=1      #진입차수 정보모음

q=deque()
basic_parts=[]
for i in range(1,N+1):
    if indegree[i]==0:
        basic_parts.append(i) #기본부품 리스트
        q.append(i)

while q:
    now=q.popleft()
    for object, n in E[now]:
        if now in basic_parts:   # 기본부품일경우 목적제품에 +n개
            needs[object][now]+=n
        else:
            for i in range(1,N+1):
                needs[object][i]+=needs[now][i]*n
        indegree[object]-=1
        if indegree[object]==0:
            q.append(object)

for i in range(N+1):
    if needs[N][i] > 0:
        print(i,needs[N][i])