import sys
sys.stdin=open("./boj/test_case.txt")
input = sys.stdin.readline
n = int(input())
honey = list(map(int, input().strip().split()))

from copy import deepcopy
cum_sum = deepcopy(honey)

for i in range(1, n):
    cum_sum[i] += cum_sum[i-1]

# 시나리오 별로 최대 꿀의 합 계산
# 시나리오 1: 꿀통이 벌들 가운데 있으면, 벌들은 맨 끝에 있는게 최대값. (전체 꿀의 합 중 처음 끝 제외) + (꿀통 위치 꿀) -> 즉, 꿀통 위치는 꿀이 최대인 곳
answer = cum_sum[-1]-honey[0]-honey[-1]+max(honey[1:-1])

# 시나리오 2, 3: 꿀통이 벌들의 왼쪽 혹은 오른쪽에 있을 때. 꿀통은 왼쪽 끝 혹은 오른 쪽 끝 둘 중 하나. 그리고 벌 한마리는 다른 쪽 끝. 나머지 한마리만 배치하면 됨.
for bee in range(1, n-1):
    answer = max(answer, cum_sum[-1]-honey[0]-honey[bee]+cum_sum[-1]-cum_sum[bee])
for bee in range(1, n-1):
    answer = max(answer, cum_sum[-1]-honey[-1]-honey[bee]+cum_sum[bee-1])
print(answer)
