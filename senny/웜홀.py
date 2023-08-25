# 백준 1865
# 벨만포드
# 음수 사이클이 존재하는지 판단
# 얘도 거의 보고 풀었다
# 3중 for문을 사용하면 틀린다
import sys
input = sys.stdin.readline

def bellman():
    for i in range(N):
        for j in range(len(edges)):
            now, next, cost = edges[j]
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                if i == N - 1:
                    return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    dist = [sys.maxsize] * (N+1)
    for i in range(M + W):
        S, E, T = map(int, input().split()) # S, E : 연결된 지점의 번호, T : 걸리는 시간
        if i >= M:
            T = -T # M번 이후에 받는 T는 줄어드는 시간
        else: #M번 이전에 받은 경우
            edges.append((E, S, T)) # 종료점, 시작점, 줄어드는 시간 순으로 append
        edges.append((S, E, T)) # 시작점, 종료점, 소요 시간 순으로 append
    if bellman():
        print("YES")
    else:
        print("NO")