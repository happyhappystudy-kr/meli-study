import sys
input = sys.stdin.readline

n = int(input().strip())
cranes = list(map(int, input().strip().split()))
m = int(input().strip())
boxes = list(map(int, input().strip().split()))

boxes.sort(reverse=True)
cranes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit(0)

crane_pos = 0
box_pos = 0
answer = 0
while boxes:
    if box_pos >= len(boxes) or crane_pos >= n:
        box_pos = 0
        crane_pos = 0
        answer += 1
        continue
    if boxes[-1] > cranes[crane_pos]:
        box_pos = 0
        crane_pos = 0
        answer += 1
        continue
    if boxes[box_pos] <= cranes[crane_pos]:
        boxes.pop(box_pos)
        crane_pos += 1
        if len(boxes) == 0:
            answer += 1
        continue
    box_pos += 1
print(answer)