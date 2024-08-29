n = int(input().strip())
towers = list(map(int, input().strip().split(" ")))
indices = list(range(1, n+1))
answer = [0]*n

import heapq
towers_heap = []
for i in range(-1, -n-1, -1):
    height = towers[i]
    pos = indices[i]
    while towers_heap and towers_heap[0][0] < height:
        _, idx = heapq.heappop(towers_heap)
        answer[idx] = pos
    heapq.heappush(towers_heap, (height, i))

print(" ".join(list(map(str, answer))))