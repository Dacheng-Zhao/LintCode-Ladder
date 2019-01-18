import collections
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    
    # [4: [1]]]  [1: [5]]
    # [4: 0]  [1: 1]
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = collections.defaultdict(list)
        nb_dependent =  collections.defaultdict(int)
        
        for seq in seqs:
            if len(seq) == 1:
                graph[seq[0]].append(0)
                nb_dependent[seq[0]] += 0
            else:
                for i in range(len(seq) - 1):
                    graph[seq[i]].append(seq[i + 1])
                    nb_dependent[seq[i + 1]] += 1
                    if i == 0:
                        nb_dependent[seq[i]] += 0
                
        can_take = []
        for k, v in nb_dependent.items():
            if v == 0:
                can_take.append(k)
        if len(can_take) > 1:
            return False
        result = []
        
        while can_take:
            first_number = can_take.pop()
            result.append(first_number)
            
            for dependent in graph[first_number]:
                nb_dependent[dependent] -= 1 
                if nb_dependent[dependent] == 0:
                    can_take.append(dependent)
        print(result)
        return result == org
            
            
                
        
        



                
            
