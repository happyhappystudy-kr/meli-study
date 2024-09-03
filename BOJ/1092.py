import sys
sys.stdin = open("test_case.txt")
input = sys.stdin.readline

n = int(input().strip())
cranes = list(map(int, input().strip().split()))
m = int(input().strip())
boxes = list(map(int, input().strip().split()))

boxes.sort()
cranes.sort()
if cranes[-1] < boxes[-1]:
    print(-1)
    exit(0)


# 시간 초과
boxes.sort(reverse=True)
cranes.sort(reverse=True)
crane_pos = 0
box_pos = 0
answer = 0
while boxes:
    if box_pos >= len(boxes) or crane_pos >= n:
        box_pos = 0
        crane_pos = 0
        answer += 1
    if boxes[box_pos] <= cranes[crane_pos]:
        boxes.pop(box_pos)
        box_pos -= 1
        crane_pos += 1
        if len(boxes) == 0:
            answer += 1
    box_pos += 1
print(answer)