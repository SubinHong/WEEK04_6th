# import sys

# string_a = ' ' + sys.stdin.readline().rstrip()
# string_b = ' ' + sys.stdin.readline().rstrip()
# dp = [[0] * len(string_b) for _ in range(len(string_a))]

# for i in range(1, len(string_a)):
#     for j in range(1, len(string_b)):
#         if string_a[i] == string_b[j]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print(dp[-1][-1])

# # 확실히 이해해야 함. 일단 넘어가기


"""숏코딩"""
r=lambda:map(int,input().split())
N,K=r()
D=[0]*(K+1)
for w,v in(r()for _ in range(N)):
 for m in range(K,1,-1):
  if w<=m:D[m]=max(D[m],D[m-w]+v)
print(D[K])