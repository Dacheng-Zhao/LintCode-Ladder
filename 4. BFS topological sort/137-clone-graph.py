"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    # def cloneGraph(self, node):
    #     # write your code here
    #     root = node
    #     if node is None:
    #         return node
    #     print(node.neighbors.label) 
    #     # use bfs algorithm to traverse the graph and get all nodes.
    #     nodes = self.BFS(node)
        
    #     # copy nodes, store the old->new mapping information in a hash map
    #     mapping = {}
    #     for node in nodes:
    #         mapping[node] = UndirectedGraphNode(node.label)
        
    #     # copy neighbors(edges)
    #     for node in nodes:
    #         new_node = mapping[node]
    #         for neighbor in node.neighbors:
    #             new_neighbor = mapping[neighbor]
    #             new_node.neighbors.append(new_neighbor)
        
    #     return mapping[root]
        
        
    # def BFS(self, node):
    #         q = [node]
    #         result = set([node])
    #         while q:
    #             head = q.pop()
    #             for neighbor in head.neighbors:
    #                 if neighbor not in result:
    #                     result.add(neighbor)
    #                     q.append(neighbor)
    #         return result
        
    def cloneGraph(self, node):
        root = node
        if not node:
            return None
        
        # find all nodes
        nodes = self.BFS(node)
        
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
            
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        print(mapping[root])
        return mapping[root]
        
    def BFS(self, node):
        q = collections.deque()
        q.append(node)
        result = collections.deque()
        result.append(node)
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.append(neighbor)
                    q.append(neighbor)
        return result
            