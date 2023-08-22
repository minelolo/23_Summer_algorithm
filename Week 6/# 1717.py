import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
        
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b and a < b:
        parent[b] = a

def check(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(m):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if check(a, b):
            print("YES")
        else:
            print("NO")