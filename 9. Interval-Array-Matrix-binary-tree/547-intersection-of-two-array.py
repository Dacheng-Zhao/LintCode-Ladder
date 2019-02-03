class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        # if not nums1 or not nums2:
        #     return []
        # exceed time limit   
        # dictres = {}
        # res = []
        # for i in range(len(nums1)):
        #     if nums1[i] not in dictres:
        #         dictres[nums1[i]] = 0
        #     else:
        #         dictres[nums1[i]] += 1 
        
        # for j in range(len(nums2)):
        #     if nums2[j] in dictres and nums2[j] not in res:
        #         res.append(nums2[j])
        # return res
        # return list(set(nums1) & set(nums2))
        
        fin = []
        dic1 = {num: n for n, num in enumerate(nums1)}
        dic2 = {num: n for n, num in enumerate(nums2)}
        if len(nums1)>len(nums2):
            for i in dic2:
                if i in dic1:
                    fin.append(i)
        else:
            for i in dic1:
                if i in dic2:
                    fin.append(i)
        return fin