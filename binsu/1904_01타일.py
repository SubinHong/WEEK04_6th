from sys import stdin
input = stdin.readline

N = int(input())

# Top-Down 피보나치 접근
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

# 나머지 구하기
for i in range(3, N+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[N])
