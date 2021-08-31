from sys import stdin

input = stdin.readline

# 테스트 케이스 T
T = int(input())

for i in range(0, T):
    # 선발인원 누적해줄 cnt
    cnt = 1
    newcome = []
    # 지원자 수 N
    N = int(input())

    for i in range(N):
        resume, interv = map(int, input().split())
        newcome.append([resume, interv])

    # 서류시험 기준[][0]으로 오름차순 sort
    newcome.sort()
    maximum = newcome[0][1]

    for i in range(1, N):
        if maximum > newcome[i][1]:
            cnt += 1
            maximum = newcome[i][1]

    print(cnt)
