# from collections import deque

# def solution(tickets):
#     answer = []
#     //start = "ICN"
#     flight = []
    
#     for from, to in tickets:
#         if from in flight:
#             flight[from].append(to)
#         else:
#             flight[from] = to
            
#     def dfs(from):
#         while flight[from]:
            
from collections import defaultdict

def solution(tickets):
    flights = defaultdict(list)

    # 모든 티켓을 각 출발점에 따라 정렬하여 저장합니다.
    for start, end in sorted(tickets):
        flights[start].append(end)

    routes = []

    def dfs(start, path):
        path.append(start)

        # 모든 티켓을 사용했다면, 현재 경로를 가능한 경로에 추가합니다.
        if len(path) == len(tickets) + 1:
            routes.append(path.copy())
            return

        for i in range(len(flights[start])):
            next = flights[start].pop(i)
            dfs(next, path)
            path.pop()
            flights[start].insert(i, next) 

    dfs('ICN', [])

    return min(routes) 
        