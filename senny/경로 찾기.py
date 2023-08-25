# 백준 11403
import sys
input = sys.stdin.readline
# 길이가 양수인 경로가 있는지 없는지
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드 워셜의 핵심은 3중 for문
for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for i in range(N):
    for j in range(N):
        print(graph[i][j], end = ' ')
    print()