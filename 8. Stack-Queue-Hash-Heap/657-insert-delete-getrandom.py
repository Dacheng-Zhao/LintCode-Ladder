import random
class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.l = []
        self.d = {}
    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.d:
            return False
        deleteIndex = self.d[val]
        newVal = self.l[-1]
        self.l[deleteIndex] = newVal
        self.d[newVal] = deleteIndex
        self.l.pop()
        del self.d[val]
        return True
    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()