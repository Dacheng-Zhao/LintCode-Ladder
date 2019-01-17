from collections import defaultdict
import collections

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        # DFS
        graph = collections.defaultdict(set)
        for k, v in prerequisites:
            graph[v].add(k)
        marks = [0] * numCourses

        def dfs(i):
            if marks[i] == 2:
                return True
            if marks[i] == 0:
                marks[i] = 1
            for u in graph[i]:
                if marks[u] == 1:
                    return False
                elif not dfs(u):
                    return False
            marks[i] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    # BFS
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        nb_prerequisites = defaultdict(int)
        for k, v in prerequisites:
            graph[v].append(k)
            nb_prerequisites[k] += 1
        can_take = set(i for i in range(numCourses)) - set(nb_prerequisites.keys())
        
        while can_take:
            course = can_take.pop()
            numCourses -= 1 
            for dependent in graph[course]:
                nb_prerequisites[dependent] -= 1 
                if nb_prerequisites[dependent] == 0:
                    can_take.add(dependent)
        return numCourses == 0


