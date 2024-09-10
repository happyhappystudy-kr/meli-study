import sys
import heapq
sys.stdin=open("./boj/test_case.txt","r")
input = sys.stdin.readline
n = int(input())
classes = []
for _ in range(n):
    heapq.heappush(classes, list(map(int, input().strip().split())))

end_times = []
while classes:
    l = heapq.heappop(classes)

    if end_times and end_times[0] <= l[0]:
        heapq.heappop(end_times)
    heapq.heappush(end_times, l[1])

print(len(end_times))