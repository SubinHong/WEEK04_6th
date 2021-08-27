import sys

meeting_N = int(sys.stdin.readline().strip())

meeting_data = []

for _ in range(meeting_N):
    start, end = map(int, sys.stdin.readline().strip().split())
    meeting_data.append((start, end))

print(meeting_data)