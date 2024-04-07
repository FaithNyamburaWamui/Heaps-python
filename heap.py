import heapq

d = [15,6,17,10,12,20,21,43,45]
heapq.heapify(d)
print(d)

heapq.heappush(d,8)
print(d)

heapq.heappop(d)
print(d)