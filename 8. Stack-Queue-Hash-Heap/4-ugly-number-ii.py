import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        # res = [1]
        # p1, p2, p3 = 0, 0, 0
        
        # while len(res) < n:
        #     temp1 = res[p1] * 2
        #     temp2 = res[p2] * 3
        #     temp3 = res[p3] * 5
            
        #     actual = min(temp1, temp2, temp3)
            
        #     if actual == temp1:
        #         p1 += 1 
        #     if actual == temp2:
        #         p2 += 1 
        #     if actual == temp3:
        #         p3 += 1 
            
        #     res.append(actual)
        # return res[n - 1]
        
        heap = [1]
        base = None
        for i in range(n):
            base = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if base * factor not in heap:
                    heapq.heappush(heap, (base * factor))
                    
        return base