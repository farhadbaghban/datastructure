import heapq
li = [1, 12, 23, 41, 5, 6, 15, 2]
# create a min heap
heapq.heapify(li)
print(list(li))
# push a member
heapq.heappush(li, 99)
print(list(li))
heapq.heappush(li, 0)
print(list(li))
heapq.heappush(li, 13)
print(list(li))
# pop a member
heapq.heappop(li)
print(list(li))
# simultaneously push and pop
print(heapq.heappushpop(li, 3))
print(list(li))
print(heapq.heapreplace(li, 49))
print(list(li))
# number of largest members
print(heapq.nlargest(3, li))
# number of lowest members
print(heapq.nsmallest(3, li))
