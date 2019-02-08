import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        
        # if not arrays:
        #     return []
        
        # oneDarray = []
        # for i in range(len(arrays)):
        #     for j in range(len(arrays[i])):
        #         oneDarray.append(arrays[i][j])
        
        # oneDarray.sort()
        # return oneDarray
        
        if not arrays or not arrays[0]:
            return []
        
        h = []
        for i in range(len(arrays)):
            for j in range(len(arrays[i])):
                heapq.heappush(h, arrays[i][j])
        return [heapq.heappop(h) for _ in range(len(h))]