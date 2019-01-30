"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        points = sorted(points, key = lambda p: p.x + p.y)
        return sorted(points, key = lambda p: ((p.x-origin.x)**2 + (p.y-origin.y)**2))[0:k]
        
        # dic = {}
        
        # for i in range(len(points)):
        #     dic[points[i][0]**2 + points[i][1]**2] = i
        
        # sortedArray = sorted(dic)
        # returnedArray = []
        # for j in range(k):
        #     returnedArray.append(points[dic[sortedArray[j]]]) 
        # return returnedArray