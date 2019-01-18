"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        
        # following_nodes = {x: 0 for x in graph}
        # for node in graph:
        #     for neighbor in node.neighbors:
        #         following_nodes[neighbor] += 1 
                
        # result = []
        # start_node = [n for n in graph if following_nodes[n] == 0]
        # queue = collections.deque(start_node)
        
        # while queue:
        #     node = queue.popleft()
        #     result.append(node)
        #     for neighbor in node.neighbors:
        #         following_nodes[neighbor] -= 1
        #         if following_nodes[neighbor] == 0:
        #             queue.append(neighbor)
                
        # return result
        
        nb_dependent = collections.defaultdict(int)
        for node in graph:
            nb_dependent[node] += 0
            for neighbor in node.neighbors:
                nb_dependent[neighbor] += 1
        
        result = []
        start_node = collections.deque()
        for k, v in nb_dependent.items():
            if nb_dependent[k] == 0:
                start_node.append(k)
        
        while start_node:
            node = start_node.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                nb_dependent[neighbor] -= 1 
                if nb_dependent[neighbor] == 0:
                    start_node.append(neighbor)
        return result