class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here
        if not J or not S:
            return 0 
        
        jewelsMap = {}
        res = 0
        
        for ele in J:
            if ele not in jewelsMap:
                jewelsMap[ele] = 1
                
        for ele in S:
            if ele in jewelsMap:
                res += 1 
        return res 
        