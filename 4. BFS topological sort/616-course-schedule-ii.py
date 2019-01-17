from collections import defaultdict

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        graph = defaultdict(list)
        nb_prerequisites = defaultdict(int)
        for k, v in prerequisites:
            graph[v].append(k)
            nb_prerequisites[k] += 1
        can_take = set(i for i in range(numCourses)) - set(nb_prerequisites.keys())
        result = []
        while can_take:
            numCourses -= 1
            course = can_take.pop()
            result.append(course)
            for dependent in graph[course]:
                nb_prerequisites[dependent] -= 1
                if nb_prerequisites[dependent] == 0:
                    can_take.add(dependent)
        if numCourses == 0:
            return result
        else:
            return []