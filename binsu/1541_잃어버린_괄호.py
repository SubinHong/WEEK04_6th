from sys import stdin

input = stdin.readline

# expr(식) 배열에 - 기준으로 split되어 저장
expr = input().split('-')

result = 0

# 처음 -가 나오기 전까지의 숫자(0번째 인덱스)들은 전부 더함
for i in expr[0].split('+'):
    result += int(i)

# -가 나오면 뒤의 모든 수를 빼줌
for i in expr[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
