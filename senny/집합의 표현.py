# 백준 1717
# 교재 필사
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sys.setrecursionlimit(1000000) # 재귀 함수 형태

# 집합 초기화 : 인덱스 값으로
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

# find 연산
def find(a):
    if a == parent[a]: #index와 value가 같다면
        return a
    else:
        parent[a] = find(parent[a]) #다르다면 같을 때까지 반복
        return parent[a]

# union 연산
def union(x, y):
    x = find(x) #x의 대표 노드 찾기
    y = find(y) #y의 대표 노드 찾기
    if x != y:  #대표 노드가 다르다면
        parent[y] = x #대표노드 업데이트

# 두 원소가 같은 집합에 있는지 확인
def check(x,y): 
    x = find(x) #x의 대표 노드 찾기
    y = find(y) #y의 대표 노드 찾기
    if x == y: #대표 노드가 같다면 같은 집합
        return True
    return False

for _ in range(m):
    order, a, b = map(int, input().split())
    if order == 0: # 합집합 연산
        union(a, b)
    else: #출력
        if check(a, b) == True:
            print("yes")
        else:
            print("no")