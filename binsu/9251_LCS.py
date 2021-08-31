A, B = input(), input()
dp = [0]*len(B)

for i in range(len(A)):
    max_dp = 0
    for j in range(len(B)):
        if max_dp < dp[j]:
            max_dp = dp[j]
        elif A[i] == B[j]:
            dp[j] = max_dp+1
print(max(dp))
