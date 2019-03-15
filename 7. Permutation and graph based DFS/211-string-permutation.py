# class Solution:
#     """
#     @param A: a string
#     @param B: a string
#     @return: a boolean
#     """
#     def Permutation(self, A, B):
#         # write your code here
        
#         # exceeded time limit
#     #     self.res = []
#     #     listA = list(A)
#     #     self.DFS(listA, 0)
#     #     return B in self.res
        
#     # def DFS(self, A, index):
#     #     if index == len(A):
#     #         return self.res.append(''.join(A[:]))
        
#     #     for i in range(index, len(A)):
#     #         A[i], A[index] = A[index], A[i]
#     #         self.DFS(A, index + 1)
#     #         A[i], A[index] = A[index], A[i]
        
        
#         # self.dictcheck = {}
#         if A == '' and B == '':
#             return True
#         if not A or not B:
#             return False
            
#         # for i in A:
#         #     if i in self.dictcheck:
#         #         self.dictcheck[i] += 1 
#         #     else:
#         #         self.dictcheck[i] = 1
        
#         # for j in B:
#         #     if j in self.dictcheck:
#         #         self.dictcheck[j] -= 1 
#         #     else:
#         #         return False
        
#         # for k, v in self.dictcheck.items():
#         #     if v != 0:
#         #         return False
        
#         # return True
        
#         # exceeded time limit
#         listA = list(A)
#         permutationList = self.DFS(listA)
#         res = []
        
#         for x in permutationList:
#             res.append(''.join(x))
#         return B in res
        
        
#     def DFS(self, A):
#         if len(A) == 0:
#             return []
            
#         if len(A) == 1:
#             return [A]
            
#         l = []
        
#         for i in range(len(A)):
#             m = A[i]
#             remain = A[ : i] + A[i + 1 :]
            
#             for p in self.DFS(remain):
#                 l.append([m] + p)
#         return l
        
class Solution:
    def Permutation(self, nums):
        if not nums:
            return []
        self.numsLen = len(nums)
        self.res = []
        self.DFS(nums, [])
        return self.res

    def DFS(self, remain, temp):
        if not remain:
            return 
        
        for i in range(len(remain)):
            remaining = remain[:i] + remain[i + 1 :]
            temp.append(remain[i])
            if len(temp) == self.numsLen:
                self.res.append(temp[:])
            self.DFS(remaining, temp)
            temp.pop()

test = Solution()
print(test.Permutation([1,2,3]))

