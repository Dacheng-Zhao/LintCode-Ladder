from collections import defaultdict
class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """
    def killProcess(self, pid, ppid, kill):
        # Write your code here
        parentChildMap = defaultdict(list)
        numberOfChild = defaultdict(int)
        for i in range(len(ppid)):
            parentChildMap[ppid[i]].append(pid[i])
            numberOfChild[ppid[i]] += 1 
        
        stack = [parentChildMap[kill]]
        res = [kill]
        
        while stack:
            children = stack.pop()
            res += children
            for i in range(len(children)):
                if numberOfChild[children[i]] != 0:
                    stack.append(parentChildMap[children[i]])
        return res
