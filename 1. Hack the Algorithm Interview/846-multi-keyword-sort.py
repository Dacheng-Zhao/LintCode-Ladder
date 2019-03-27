class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        # Write your code here
        if not array:
            return []
            
        studentDict = {}
        
        for ele in array:
            if ele[1] not in studentDict:
                studentDict[ele[1]] = [ele[0]]
            else:
                studentDict[ele[1]].append(ele[0])
                studentDict[ele[1]].sort()
                
        newStudentDict = sorted(studentDict.items(), reverse = True)
        res = []

        for key, val in newStudentDict:
            for ele in val:
                res.append([ele, key])
        return res
