class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    nums = []
        
    def add(self, number):
        # write your code here
       self.nums.append(number)
        

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        dic = {}
        for i in range(len(self.nums)):
            if self.nums[i] in dic:
                return True
            else:
                dic[value - self.nums[i]] = i
        return False


        # two pointers
    """
    @param number: An integer
    @return: nothing
    """
    nums = []
        
    def add(self, number):
        # write your code here
       self.nums.append(number)
        

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        left = 0
        right = len(self.nums) - 1
        self.nums.sort()
        
        while left < right:
            temp = self.nums[left] + self.nums[right]
            if temp == value:
                return True
            elif temp < value:
                left += 1 
            else:
                right -= 1
        return False 
        