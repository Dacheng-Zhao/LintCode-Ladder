class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        self.res = []
        temp = []
        candidates.sort()
        
        def DFS(candidates, temp, target, index):
            if target == 0:
                self.res.append(temp[:])
            
            for i in range(index, len(candidates)):
                if target < candidates[i]:
                    return
                if i != index and candidates[i] == candidates[i-1]:
                    continue;
                temp.append(candidates[i])
                DFS(candidates, temp, target - candidates[i], i)
                temp.pop()
                
        DFS(candidates, [], target, 0)
        return self.res