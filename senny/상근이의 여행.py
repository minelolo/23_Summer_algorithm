# 백준 9372
# 모든 국가가 연결되어 있기 때문에 N-1을 출력하면 끝이라고 함.. 좀 이상한 문제 같다
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N-1)