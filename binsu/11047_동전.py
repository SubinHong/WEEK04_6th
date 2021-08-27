from sys import stdin
input = stdin.readline

# 코인 개수 입력을 위한 변수
num = 0


# 동전 개수 N과, 만들어야 할 K원
N, K = map(int, input().split())

# 돈 배열
money = [int(input()) for _ in range(N)]


for i in range(1, N+1):
    coin = money[-i]

    if K >= coin:
        mok = K//coin
        K -= coin*mok
        num += mok

print(num)

# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-11047%EB%B2%88-%EB%8F%99%EC%A0%84-0Python
