import heapq
for _ in range(int(input())):
    input()
    lst = [int(val) for val in input().split()]
    bonus = []
    res = 0
    for i in lst: # Everyone is using heapq , because it sorts the elements in place.
        if i > 0:
            heapq.heappush(bonus, -i) # If the value is bigger than others,  it will be on top of the queue as we are adding it's negative value.
        elif len(bonus) > 0:
            res -= heapq.heappop(bonus) # Heap pop always returns the smallest element.

    print(res)


