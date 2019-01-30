import collections

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.queue = collections.deque()
        self.queueSum = 0
        
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self.queue) >= self.size:
            self.queueSum -= self.queue.popleft()
        self.queue.append(val)
        self.queueSum += val
        return self.queueSum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)