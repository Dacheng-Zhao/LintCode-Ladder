from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        # write your code here
        graph = defaultdict(list)
        
        for i in range(len(flights)):
            if flights[i][1] not in graph[flights[i][0]]:
                graph[flights[i][0]].append([flights[i][1], flights[i][2]])
        
        pqueue = []
        heappush(pqueue, [0, src, 0])
        
        while pqueue:
            node = heappop(pqueue)
            if node[1] == dst:
                return node[0]
            if node[2] > K:
                continue
            if node[1] in graph:
                for i in range(len(graph[node[1]])):
                    heappush(pqueue, [node[0] + graph[node[1]][i][1], graph[node[1]][i][0], node[2] + 1])
        return -1
        
        