import heapq


def solution(n, works):
    heap = []
    for i in works:
        heapq.heappush(heap,-i)

    while n>0:
        h = -heapq.heappop(heap)
        if h != 0:
            h -=1
        heapq.heappush(heap,-h)
        n-=1

    ans = 0
    for i in heap:
        ans += i*i
    return ans