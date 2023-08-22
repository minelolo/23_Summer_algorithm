#백준 1717
import sys
input = sys.stdin.readline

#변수 입력 및 그래프 선언
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

#find 함수 선언
def find(a, parent):
    if parent[a] == a:
        return a
    return find(parent[a], parent)

#union 함수 선언
def union(a, b, parent):
    aroot = find(a, parent)
    broot = find(b, parent)

    if aroot <= broot:
        parent[broot] = aroot
    else:
        parent[aroot] = broot

#연산 입력
for _ in range(m):
    a = list(map(int, input().split()))

if a[0] == 0:
    union(a[1], a[2], parent)
elif a[0] == 1:
    if find(a[1], parent) == find(a[2], parent):
        print('YES')
    else:
        print('NO')