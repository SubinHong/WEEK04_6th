""" 코드 가독성 안좋음"""

from sys import stdin
input = stdin.readline

# 코인 개수 입력을 위한 변수
num = 0


# 동전 개수 N과, 만들어야 할 K원
N, K = map(int, input().split())

money = [int(input()) for _ in range(N)]


for i in range(1, N+1):
    coin = money[-i]

    if K >= coin:
        mok = K//coin
        K -= coin*mok
        num += mok

print(num)
